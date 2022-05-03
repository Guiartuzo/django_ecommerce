from datetime import datetime
from django.test import TestCase
from produto.models import Produto, Variacao
from perfil.models import Perfil
from pedido.models import Pedido, ItemPedido
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf

class TestProdutoModels(TestCase):

    def setUp(self):
        self.produto1 = Produto.objects.create(
            nome='test-product',
            descricao_curta='dummy-description',
            descricao_longa='dummy-description',
            preco_marketing = 0
        )

        self.variacao1 = Variacao.objects.create(
            produto = self.produto1,
            nome = 'test-variacao',
            preco = 100
        )

    def test_produto_is_created(self):
        self.assertEquals(self.produto1.slug, 'test-product')

    def test_variacao_is_created(self):
        self.assertEquals(self.variacao1.produto, self.produto1)


class TestPerfilModels(TestCase):
    
    def setUp(self):

        self.user = User.objects.create(
            username='test-user',
            password = '12345',
        )
        
        self.perfil = Perfil.objects.create(
            usario=self.user,
            idade=18,
            data_nascimento=datetime.strptime('01/01/1990','%d/%m/%Y'),
            cpf='63386070000',
            endereco='test-endereco',
            numero='12345',
            complemento='teste-complemento',
            bairro='teste-bairro',
            cep='12345678',
            cidade='teste-cidade',
        )

    def test_produto_is_created(self):
        self.assertEquals(self.perfil.estado, 'SP')
        self.assertEquals(self.perfil.usario.username, 'test-user')
        self.assertTrue(valida_cpf(self.perfil.cpf))


class TestPedidoModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test-user',
            password = '12345',
        )

        self.pedido = Pedido.objects.create(
            usuario = self.user,
            total = 1.0,
        )

        self.itemPedido = ItemPedido.objects.create(
            pedido = self.pedido,
            produto = 'teste-produto',
            produto_id = 1,
            variacao = 'teste-variacao',
            variacao_id = 1,
            preco= 1.0,
            imagem='100'
        )
        
    def test_pedido_is_created(self):
        self.assertEquals(self.pedido.usuario.username, 'test-user')
        self.assertEquals(self.pedido.status, 'C')

    def test_item_pedido_is_created(self):
        self.assertEquals(self.itemPedido.pedido.usuario.username, 'test-user')
        self.assertEquals(self.itemPedido.preco_promocional, 0)