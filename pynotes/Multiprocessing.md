# Pyhton Multiprocessing

##[Python标准库10 多进程初步 (multiprocessing包)](http://www.cnblogs.com/vamei/archive/2012/10/12/2721484.html)

### Limitations of Subprocess
我们已经见过了使用subprocess包来创建子进程，但这个包有两个很大的局限性：<br>
1) 我们总是让subprocess运行外部的程序，而不是运行一个Python脚本内部编写的函数。<br>
2) 进程间只通过管道进行文本交流。<br>
以上限制了我们将subprocess包应用到更广泛的多进程任务。(这样的比较实际是不公平的，
因为subprocessing本身就是设计成为一个shell，而不是一个多进程管理包)


### threading & multiprocessing

[Python多线程与同步](http://www.cnblogs.com/vamei/archive/2012/10/11/2720042.html)

multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process
对象来创建一个进程。该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，
也有start(), run(), join()的方法。此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 
(这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，其用法与threading包中的同名类一致。
所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。
