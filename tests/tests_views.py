from django.test import TestCase, Client
from django.urls import reverse
from produto.models import Produto, Variacao
import json

class TestProdutoViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.lista_url = reverse('produto:lista')
        self.detalhe_url = reverse('produto:detalhe', args=['test-product'])
        self.produto =Produto.objects.create(
            nome='test-product',
            descricao_curta='dummy-description',
            descricao_longa='dummy-description',
            preco_marketing = 0
        )
        self.carrinho_url = reverse('produto:carrinho')
        self.resumodacompra_url = reverse('produto:resumodacompra')

    def test_produto_list_GET(self):
        response = self.client.get(self.lista_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/lista.html')

    def test_detalheproduto_GET(self):
        response = self.client.get(self.detalhe_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/detalhe.html')

    def test_carrinho_GET(self):
        response = self.client.get(self.carrinho_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/carrinho.html')

    #TODO: uncomment as soon as implemented
    # def test_resumodacompra_GET(self):
    #     response = self.client.get(self.resumodacompra_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'produto/resumodacompra.html')


class TestPerfilViews(TestCase):
    pass


class TestPedidoViews(TestCase):
    pass
