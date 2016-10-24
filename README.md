#《神秘的程序员们》抽奖代码

这段代码利用bitcoin的随机性产生抽奖活动的中奖号码。

使用方法：

1. 在 https://blockexplorer.com 选取某个时刻的 BlockHash （具体使用哪个时刻根据抽奖活动规则确定）
2. 运行脚本 ./lotteryResult.py blockhash number total startnum 

参数说明：

* blockhash 某个时刻的BlockHash
* number 总共中奖人数，比如50个
* total 全部发出的奖券数量，比如 59391 张
* startnum 奖券号码起始值，为了奖券号码好看，一般用一个比较大的数值做为开始，我们一般采用 1000000

例子：

```
./lotteryResult.py 000000000000000003eaa089e640ea339a4f5c83721a607c1075d3443a834e84 50 59391 1000000

result 0 is 1026155
result 1 is 1055107
result 2 is 1056394
result 3 is 1010464
result 4 is 1047703
result 5 is 1033045
......
```

以上号码即为各中奖结果
