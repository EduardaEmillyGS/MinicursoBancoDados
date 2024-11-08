import DAO
from DAO import buscar_usuario

#saida = DAO.inserir_usuario("eduardasoares@gmail.com", "duda", 123)
#saida = DAO.inserir_usuario("didi@gmail.com", "Diego", 321)
#saida = DAO.buscar_usuario("duda")
#saida = DAO.listar_usuarios("duda")
#saida = DAO.atualizar_usuario(1, "doug", "teftdwvdywtevdgvd@.com")

saida = DAO.deletar_usuario("5")
print (saida)

