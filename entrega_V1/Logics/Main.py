from entrega_V1.Grafics import Front
from entrega_V1.Resources import BaseDatosLog

def main():
    Front.ventana.mainloop()

if __name__ == '__main__':
    main()
    print(BaseDatosLog.mydb)