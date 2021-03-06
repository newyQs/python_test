"""
http://c.biancheng.net/python/thread/
几乎所有的操作系统都支持同时运行多个任务，每个任务通常是一个程序，每一个运行中的程序就是一个进程，即进程是应用程序的执行实例。
现代的操作系统几乎都支持多进程并发执行。

注意，并发和并行是两个概念，并行指在同一时刻有多条指令在多个处理器上同时执行；
并发是指在同一时刻只能有一条指令执行，但多个进程指令被快速轮换执行，使得在宏观上具有多个进程同时执行的效果。

例如，程序员一边开着开发工具在写程序，一边开着参考手册备查，同时还使用电脑播放音乐……除此之外，
每台电脑运行时还有大量底层的支撑性程序在运行……这些进程看上去像是在同时工作。

但事实的真相是，对于一个 CPU 而言，在某个时间点它只能执行一个程序。
也就是说，只能运行一个进程，CPU 不断地在这些进程之间轮换执行。那么，为什么用户感觉不到任何中断呢？

这是因为相对人的感觉来说，CPU 的执行速度太快了（如果启动的程序足够多，则用户依然可以感觉到程序的运行速度下降了）。
所以，虽然 CPU 在多个进程之间轮换执行，但用户感觉到好像有多个进程在同时执行。


线程是进程的组成部分，一个进程可以拥有多个线程。
在多线程中，会有一个主线程来完成整个进程从开始到结束的全部操作，而其他的线程会在主线程的运行过程中被创建或退出。

当进程被初始化后，主线程就被创建了，对于绝大多数的应用程序来说，通常仅要求有一个主线程，但也可以在进程内创建多个顺序执行流，这些顺序执行流就是线程。

当一个进程里只有一个线程时，叫作单线程。超过一个线程就叫作多线程。

每个线程必须有自己的父进程，且它可以拥有自己的堆栈、程序计数器和局部变量，但不拥有系统资源，因为它和父进程的其他线程共享该进程所拥有的全部资源。
线程可以完成一定的任务，可以与其他线程共享父进程中的共享变量及部分环境，相互之间协同完成进程所要完成的任务。

多个线程共享父进程里的全部资源，会使得编程更加方便，需要注意的是，要确保线程不会妨碍同一进程中的其他线程。

线程是独立运行的，它并不知道进程中是否还有其他线程存在。线程的运行是抢占式的，也就是说，当前运行的线程在任何时候都可能被挂起，以便另外一个线程可以运行。

多线程也是并发执行的，即同一时刻，Python 主程序只允许有一个线程执行，这和全局解释器锁有关系，后续会做详细介绍。

一个线程可以创建和撤销另一个线程，同一个进程中的多个线程之间可以并发运行。

从逻辑的角度来看，多线程存在于一个应用程序中，让一个应用程序可以有多个执行部分同时执行，
但操作系统无须将多个线程看作多个独立的应用，对多线程实现调度和管理以及资源分配，线程的调度和管理由进程本身负责完成。

简而言之，进程和线程的关系是这样的：操作系统可以同时执行多个任务，每一个任务就是一个进程，进程可以同时执行多个任务，每一个任务就是一个线程。

"""
