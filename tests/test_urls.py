from django.test import SimpleTestCase
from django.urls import reverse, resolve
from produto.views import ListaProdutos, DetalheProduto, AdicionarAoCarrinho, RemoverDoCarrinho, Carrinho

class TestUrls(SimpleTestCase):

    def test_listaproduto_url_is_resolved(self):
        url = reverse('produto:lista')
        self.assertEquals(resolve(url).func.view_class, ListaProdutos)

    def test_adicionarAoCarrinho_url_is_resolved(self):
        url = reverse('produto:adicionaraocarrinho')
        self.assertEquals(resolve(url).func.view_class, AdicionarAoCarrinho)

    def test_removerDoCarrinho_url_is_resolved(self):
        url = reverse('produto:removerdocarrinho')
        self.assertEquals(resolve(url).func.view_class, RemoverDoCarrinho)