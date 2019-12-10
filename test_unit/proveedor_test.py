import pytest
from django.utils import timezone
from proveedor.models import Proveedor

# Create your tests here.

#import proveedor.models.Proveedor as Proveedor
#from proveedor.models import PedidoProveedor
#from proveedor.models import DetallePedidoProveedor
#from proveedor.models import DevolucionPedidoProveedor
#from proveedor.models import DetalleDevolucionPedidoProveedor

class TestProveedor:
    def setUp(self):
        self.Pv=Proveedor()
        self.Pv.codigo=1233
        self.Pv.nit="ya jale"
        self.Pv.nombre = "Jean Carlos"
        self.Pv.telefono= "954234341"
        self.Pv.direccion = "jiron de la union"
        self.Pv.save()
    
    def testdatabase(self):
        all_database=self.Pv.objects.all()
        assert len(all_database) == 1
        only_database=all_database[0]

        assert only_database == Pv

"""
class TestPedidoProveedor:
    def setUp(self):
        Pv=Proveedor()
        Pv.codigo=1233
        Pv.nit="ya jale"
        Pv.nombre = "Jean Carlos"
        Pv.telefono= "954234341"
        Pv.direccion = "jiron de la union"
        Pv.save()
        
        self.PP=PedidoProveeedor()
        self.PP.proveedor=Pv
        self.PP.total_pagado=234
        
    def testdatabase(self):
        all_database=self.PP.objects.all()
        assert len(all_database) == 1

"""
