'''
现代操作系统(Windows, Mac OS X, Linux, UNIX等)都支持'多任务'

什么叫多任务？？？
操作系统同时可以运行多个任务

单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us，切换到微信，再执行2us，再切换到陌陌，执行2us......。表面上看，每个任务反复执行下去，但是CPU调度执行速度太快了，以至于我们感觉就像所有任务都在同时执行一样

多核CPU实现多任务原理：真正的并行执行多任务只能在多核CPU实现，但是由于任务数量远远大于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行
并发：看上去一起执行，任务数大于CPU的核心数
并行：真正一起执行，任务数小于等于CPU的核心数

实现多任务的方式：
1、多进程模式
2、多线程模式
3、协程模式
4、多进程+多线程模式
'''