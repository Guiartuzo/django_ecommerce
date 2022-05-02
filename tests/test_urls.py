from lib2to3.pgen2.literals import simple_escapes
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from produto.views import ListaProdutos, DetalheProduto, AdicionarAoCarrinho, RemoverDoCarrinho, Carrinho, ResumoDaCompra
from pedido.views import Pagar, Detalhes, SalvarPedido
from perfil.views import Criar, Atualizar, Login, Logout

class TestProdutoUrls(SimpleTestCase):

    def test_listaproduto_url_is_resolved(self):
        url = reverse('produto:lista')
        self.assertEquals(resolve(url).func.view_class, ListaProdutos)

    def test_adicionarAoCarrinho_url_is_resolved(self):
        url = reverse('produto:adicionaraocarrinho')
        self.assertEquals(resolve(url).func.view_class, AdicionarAoCarrinho)

    def test_removerDoCarrinho_url_is_resolved(self):
        url = reverse('produto:removerdocarrinho')
        self.assertEquals(resolve(url).func.view_class, RemoverDoCarrinho)

    def test_product_detail_url_is_resolved(self):
        url = reverse('produto:detalhe', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, DetalheProduto)

    def test_carrinho_url_is_resolved(self):
        url = reverse('produto:carrinho')
        self.assertEqual(resolve(url).func.view_class, Carrinho)

    def test_resumodacompra_url_is_resolved(self):
        url = reverse('produto:resumodacompra')
        self.assertEqual(resolve(url).func.view_class, ResumoDaCompra)
    

class TestPedidoUrls(SimpleTestCase):
    
    def test_pagar_url_is_resolved(self):
        url = reverse('pedido:pagar')
        self.assertEqual(resolve(url).func.view_class, Pagar)

    def test_salvarpedido_url_is_resolved(self):
        url = reverse('pedido:salvarpedido')
        self.assertEqual(resolve(url).func.view_class, SalvarPedido)

    def test_detalhes_url_is_resolved(self):
        url = reverse('pedido:detalhes')
        self.assertEqual(resolve(url).func.view_class, Detalhes)


class TestPerfilUrls(SimpleTestCase):

    def test_criarPerfil_url_is_resolved(self):
        url = reverse('perfil:criar')
        self.assertEqual(resolve(url).func.view_class, Criar)

    def test_atualizarPerfil_url_is_resolved(self):
        url = reverse('perfil:atualizar')
        self.assertEqual(resolve(url).func.view_class, Atualizar)
    
    def test_login_url_is_resolved(self):
        url = reverse('perfil:login')
        self.assertEqual(resolve(url).func.view_class, Login)

    def test_logout_url_is_resolved(self):
        url = reverse('perfil:logout')
        self.assertEqual(resolve(url).func.view_class, Logout)