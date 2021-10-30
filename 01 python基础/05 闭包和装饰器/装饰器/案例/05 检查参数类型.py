'''
需求：
　　实现一个装饰器，用它来检查被装饰函数的参数类型；
   装饰器可以通过函数，指明函数参数类型，进行函数调用的时候，传入参数，检测到不匹配时，抛出异常


'''

from inspect import signature


def check_type(*ty_args, **ty_kwargs):
    def out_wrapper(func):
        sig = signature(func)  # 通过signature方法，获取函数形参：name, age, height
        bind_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments  # 获得装饰器传来的参数， 函数签名与之绑定，字典类型
        print(bind_types)

        def wrapper(*args, **kwargs):
            func_type = sig.bind(*args, **kwargs).arguments.items()  # 给执行函数中具体的实参进行和形参进行绑定，形成字典的形式
            print(func_type)
            for name, obj in func_type:  # 循环形参和实参字典的items()形式
                if name in bind_types:
                    if not isinstance(obj, bind_types[name]):  # 判断实参是否是指定类型数据
                        raise TypeError('%s must be %s' % (name, bind_types[name]))
            res = func(*args, **kwargs)  # 假如函数有返回值，通过此方法返回函数的返回值
            return res

        return wrapper

    return out_wrapper


@check_type(str, int, float)  # 通过装饰器实现对函数参数进行类型检查
def func(name, age, height):
    print(name, age, height)


if __name__ == '__main__':
    func('bei_men', 18, 1.75)  # 正常数据
    func('bei_men', '18', 1.75)  # 错误数据
