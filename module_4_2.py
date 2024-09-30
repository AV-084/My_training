def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() # ничего не возвращает

inner_function()    # При вызове inner_function вне test_function возникнет ошибка, т.к. inner_function
                    # определена только внутри test_function и не доступна в глобальной области видимости

test_function()     # работает