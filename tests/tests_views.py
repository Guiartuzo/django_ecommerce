from django.test import TestCase, Client
from django.urls import reverse
from produto.models import Produto


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
    
    def setUp(self):
        self.client = Client()
        self.criar_url = reverse('perfil:criar')

    def test_criar_GET(self): 
        response = self.client.get(self.criar_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil/criar.html')

class TestPedidoViews(TestCase):
    
    def SetUp(self):
        self.client = Client()
        self.detalhe_url = reverse('pedido:detalhes')
        self.pagar_url = reverse('pedido:pagar')
        self.salvarpedido_url = reverse('pedido:salvarpedido')

    #TODO : uncomment tests as soon as implemented
    # def test_detalhes_GET(self):
    #     response = self.client.get(self.detalhe_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'pedido/detalhe.html')

    # def test_pagar_GET(self):
    #     response = self.client.get(self.pagar_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'pedido/pagar.html')

    # def test_salverpedido_GET(self):
    #     response = self.client.get(self.salvarpedido_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'pedido/salvarpedido.html')
