import math
top1=[36584.3971228 , 38271.2476393 , 37544.6769292 , 37928.8906339 , 38370.2287064 , 37868.9770869 , 38695.2921609 , 37535.0672946 , 38604.241686 , 37923.1246395 , 37408.6056136 , 37557.4709699 , 38740.7777784 , 37394.5075095 , 36817.0427175 , 36945.5865618 , 38774.9350595 , 37815.2004498 , 37452.1339436 , 38561.7839483 , 38359.0048354 , 37217.1374498 , 36529.2138778 , 36982.7356091 , 36908.0565917 , 37530.4993275 , 37797.1753663 , 36535.1651966 , 37174.1421616 , 38286.3550758 , 38103.1336125 , 38313.5281311 , 36825.4461666 , 38028.191079 , 37685.4027791 , 36550.4402573 , 38548.7910672 , 38916.283196 , 38097.4565769 , 36636.6213831 , 38343.8303776 , 38507.2307951 , 38073.7923588 , 38287.7092046 , 36947.0817208 , 38692.2307415 , 37515.9576347 , 38920.2765679 , 37643.9145449 , 36666.0297368 , 38695.1500073 , 37662.6795207 , 37245.9404696 , 38908.7504133 , 38195.0278171 , 38259.0220894 , 37736.489365 , 37310.4773321 , 38503.9700142 , 37512.2979937 , 37649.0287078 , 37604.5163289 , 37972.1170752 , 37265.8800366 , 37336.4937152 , 36906.9229185 , 38816.8625294 , 38349.2889025 , 38008.6428692 , 37154.4577874 , 37713.1060277 , 37218.4792229 , 37148.1356974 , 38735.4507269 , 37748.4691068 , 38757.182709 , 37181.0609477 , 38064.6233046 , 36666.8215612 , 38330.1290046 , 37923.9923466 , 37098.7937641 , 37002.7749357 , 36832.1931159 , 37145.1032816 , 37373.2420872 , 37690.7910252 , 36968.1725987 , 37133.0405798 , 36826.5088647 , 38020.5167619 , 37293.8309967 , 38331.4147286 , 38902.5423325 , 38245.007623 , 38623.6209208 , 36736.891885 , 37024.6069771 , 37780.7143986 , 36663.6794295]
top2=[11991.5882013 , 12251.516425 , 11629.1001158 , 13435.103922 , 11399.9879235 , 13400.5907222 , 11814.4460928 , 13738.2262503 , 13294.8062646 , 13103.4347877 , 11729.4709759 , 12550.9896586 , 12694.4591148 , 12923.552671 , 13037.6029615 , 11628.2736499 , 11798.9485449 , 13375.8316485 , 13555.6143123 , 12119.6243159 , 12374.7234291 , 12390.9170669 , 12758.4782014 , 12609.0215282 , 12327.8828107 , 12454.7127388 , 13054.2584221 , 13317.787045 , 13068.9459452 , 12156.9090403 , 13515.3569492 , 11638.6018082 , 12613.685359 , 12745.5697545 , 13008.3049023 , 11938.8710759 , 12128.5570677 , 13459.0255085 , 13738.3632925 , 12074.15979 , 12022.5146085 , 12022.050882 , 13748.1150319 , 13224.4541821 , 12927.0175064 , 12425.3192985 , 12882.8632809 , 12468.5646285 , 13723.2247004 , 12128.7897001 , 13541.1448485 , 12298.9292066 , 12603.0354774 , 12990.178484 , 11564.0277272 , 12928.4372389 , 12363.9134246 , 12045.1773523 , 11665.6775551 , 13605.2749248 , 11749.641833 , 12116.1998771 , 11881.9053462 , 13115.4744755 , 12066.7386824 , 13188.1610347 , 11690.8455881 , 12601.7501427 , 12430.5201798 , 11839.3210894 , 11562.2379122 , 13766.0967183 , 12957.0302573 , 13639.116785 , 11393.081465 , 11505.5049982 , 12085.0414129 , 11393.8319288 , 11483.468878 , 12536.2319034 , 12497.9165674 , 12456.773139 , 13521.8277901 , 12111.2020843 , 11654.5598842 , 12617.9972983 , 13205.7751094 , 11805.0071757 , 13668.6696076 , 12221.7568299 , 12601.1104964 , 13611.4671756 , 12051.072146 , 12954.2471158 , 12833.475505 , 12342.8096905 , 12157.7350114 , 13370.7825478 , 11693.3073126 , 13404.2012589]
top3=[6278.57881374 , 5352.34580622 , 5858.24681559 , 7387.69895459 , 7373.93677885 , 6906.3534412 , 7346.74075575 , 6385.92894008 , 7137.40978572 , 5770.35162838 , 6789.10661265 , 6919.53767565 , 6977.40096336 , 6625.09463396 , 7195.19813689 , 5751.72314291 , 6105.90100234 , 5331.29763009 , 6288.60042535 , 6997.87888769 , 6924.13550723 , 6132.0813567 , 5993.16285535 , 5465.49615136 , 7039.9155146 , 7477.2993716 , 7358.83656227 , 6297.32167028 , 6937.51031252 , 6602.96059431 , 5428.62709581 , 6151.16401689 , 7357.0202824 , 7177.08493103 , 6458.07689943 , 6657.57950261 , 5446.65178877 , 5377.06558196 , 5931.03375254 , 6852.2111903 , 6457.58614262 , 6378.50575002 , 6979.84166577 , 6500.66446875 , 6439.70379803 , 6246.76992921 , 6417.52313026 , 5232.86504434 , 6172.07725847 , 6185.39405563 , 6570.82685597 , 6157.79405454 , 5149.68931974 , 6509.24587062 , 6070.78411634 , 5277.22405162 , 5133.39352704 , 5802.89639638 , 6934.37260562 , 5655.48900659 , 7365.08656692 , 5209.56903402 , 5523.50292312 , 6368.35888014 , 6241.17251672 , 6990.71380487 , 6017.10728683 , 7015.80010239 , 5823.60838546 , 7314.82936612 , 7173.01518373 , 6353.36167267 , 7296.24648582 , 6787.09652375 , 5957.81997543 , 5457.95969333 , 6966.26373432 , 6100.09666594 , 6557.62584475 , 7356.0374944 , 6557.40605616 , 5737.96130036 , 5379.52419067 , 5595.42322857 , 6733.65285009 , 6953.56036419 , 5909.36603343 , 6818.84693984 , 5862.24625015 , 5991.18986475 , 7067.19240351 , 5883.03893433 , 5134.09404586 , 6560.60398352 , 6317.0807159 , 5122.06745663 , 5211.89090848 , 6978.65414547 , 5950.77512105 , 5454.53109455]

top301=[7205.73736956 , 7258.53301603 , 6565.87618193 , 6929.68826168 , 6013.7196443 , 6310.60874478 , 5826.31576635 , 7233.50536691 , 6761.16356848 , 6741.45520999 , 6982.51521944 , 6217.84088387 , 5980.00220796 , 6691.29034581 , 5078.79191189 , 5730.00736128 , 5349.06190702 , 4933.05831655 , 6623.64717656 , 6315.18082885 , 5269.39749683 , 5830.68056014 , 7285.81178927 , 6444.2935823 , 6124.75764738 , 5930.57456668 , 6868.56968727 , 5279.50906912 , 6595.31762798 , 5694.69321824 , 6665.19066746 , 6745.37175564 , 4954.67913943 , 5476.82645091 , 7012.02479703 , 5836.56491689 , 6219.80202806 , 5778.54922547 , 5807.52283775 , 5479.05805139 , 4998.97367653 , 4943.82275992 , 4979.37171912 , 4946.72626881 , 5714.74561459 , 6202.30810095 , 5730.85238748 , 6747.898914 , 6085.28513886 , 6517.52426996 , 7116.8808053 , 7051.28494064 , 5133.28865051 , 5537.04335129 , 5613.24913832 , 6428.68384368 , 5188.21373064 , 5550.07711842 , 5476.45175639 , 7119.69857277 , 6810.45823738 , 5870.69001389 , 6053.83271217 , 5065.52194093 , 6510.42405644 , 5912.30113999 , 5077.58762658 , 6291.18369488 , 6409.10270408 , 5043.09111454 , 5318.34039052 , 7199.09401861 , 6261.84243712 , 5894.373571 , 5188.59515904 , 5889.12679991 , 5882.77027685 , 6819.2828825 , 7133.73810154 , 6692.30520513 , 5704.18336651 , 5982.0105326 , 7129.08766433 , 5176.43659406 , 5283.31959084 , 5761.85994154 , 5071.437768 , 6681.75314961 , 5538.57266067 , 6242.98475219 , 5122.82996179 , 6944.33821117 , 7246.70288216 , 5066.41416258 , 6899.34900246 , 6563.32133332 , 5940.83453036 , 6514.21703435 , 7059.85089231 , 5045.17226167]
top310=[6211.33036793 , 5790.11232373 , 5697.1537821 , 6640.28129966 , 5509.07188693 , 6648.20978853 , 7435.7964038 , 7199.89244566 , 6464.28952384 , 7336.02249452 , 7417.64614565 , 7414.27675574 , 5826.67737617 , 5406.23884785 , 5578.20889117 , 5817.1480359 , 6073.14734965 , 6656.87868115 , 6515.33662228 , 6235.44113824 , 6968.91227666 , 6327.03937459 , 5594.67181063 , 5198.74522011 , 7282.46074281 , 6879.37000743 , 5504.14598037 , 5279.51886061 , 6390.73712519 , 5396.2673783 , 5837.77988139 , 6335.64847585 , 5889.14241951 , 6111.6324096 , 6918.34676462 , 5855.77776279 , 6692.66885191 , 7401.45207015 , 7347.22598556 , 5829.37229179 , 5116.51781084 , 5605.19994693 , 7067.71242898 , 6375.08749591 , 5352.79690048 , 5404.38142097 , 6978.35267865 , 7334.91561144 , 6866.33127888 , 6387.23759007 , 6115.86647153 , 5450.79737215 , 5554.56434863 , 6125.8121801 , 6390.25749886 , 6631.83819199 , 5898.76754692 , 7016.42260132 , 6835.282307 , 6265.10991636 , 5178.92557486 , 6259.33779541 , 5266.22884968 , 5443.00931477 , 7308.72276208 , 7386.64418333 , 7236.38941363 , 5235.74704876 , 6766.06447058 , 6586.98251055 , 5882.55613514 , 6499.4027299 , 6094.17405864 , 5912.01799389 , 6422.86974741 , 6073.90544638 , 5126.34279658 , 5744.69925526 , 5322.01372101 , 7204.23859875 , 6574.83584087 , 5158.52371623 , 6084.55817944 , 7195.53314992 , 5528.92197679 , 5995.01518914 , 6563.73178185 , 5874.39387865 , 5873.25196085 , 6534.80516607 , 5627.34486719 , 6319.40792057 , 6182.20541676 , 6018.98447533 , 6008.05332375 , 5477.12144227 , 5962.46652206 , 7168.0814638 , 6952.7616596 , 6231.61172899]
top350=[10930.310648 , 9149.41870097 , 9967.53695458 , 9682.89506209 , 10790.3009981 , 10846.7930432 , 11203.5039111 , 11210.7436672 , 10125.4959265 , 10768.4245915 , 9987.27206569 , 8851.99732209 , 9356.89601293 , 9241.88926137 , 10912.1956704 , 11071.6651011 , 11171.9415333 , 10434.1480109 , 9677.60352648 , 10394.1352142 , 9361.7133921 , 10471.4390598 , 10608.5776703 , 8952.85009315 , 9205.05026755 , 8908.86928942 , 10572.1005226 , 9328.0138351 , 10012.9080429 , 9783.23004575 , 10226.4559011 , 9146.37500537 , 9432.36537943 , 10313.237292 , 10619.8142765 , 10289.5566934 , 10318.9260418 , 10719.7063972 , 11156.3968823 , 10428.720024 , 9118.06765908 , 10314.5617228 , 10461.0128708 , 10784.4546064 , 9760.11989798 , 9099.45294134 , 10623.6613639 , 10323.3574022 , 10447.1816992 , 10525.5651229 , 10795.2127953 , 11106.763926 , 10299.1723793 , 9169.73686086 , 10805.8233309 , 9844.25749444 , 9906.23384872 , 9881.0957524 , 10628.5581223 , 10656.2704293 , 11055.1769389 , 9335.09823278 , 9504.80213072 , 9794.87940212 , 10269.923578 , 10510.9818556 , 9611.47801833 , 10672.0699184 , 9260.99353589 , 9133.86010128 , 9185.85407018 , 9947.82396241 , 10727.3677029 , 8987.63652351 , 10856.7067195 , 8905.75842933 , 9011.93077678 , 9730.87626137 , 10175.0382605 , 9447.07527587 , 10022.0325024 , 10484.5598546 , 9764.84210742 , 9076.3019133 , 9958.73021 , 9162.20026297 , 9042.22109511 , 9393.44002085 , 9001.57605377 , 9955.34449261 , 9948.13765717 , 10178.2583235 , 10064.5833763 , 10289.3264588 , 10168.0361249 , 9018.7723651 , 9270.70038195 , 9993.21980178 , 10250.5227279 , 10930.9874095]

stats = [top1,top2,top3]
stats = [top301,top310,top350]
def average(dataSet):
    tot = 0
    for i in range(len(dataSet)):
        tot += dataSet[i]
    tot /= len(dataSet)
    return tot

def err(dataSet,avg):
    tot = 0
    for i in range(len(dataSet)):
        tot += (avg-dataSet[i])**2
    tot /= len(dataSet)
    tot = math.sqrt(tot)
    tot = tot*1.96/math.sqrt(len(dataSet))
    return tot


avgs=[]
errors=[]
for i in range(len(stats)):
    dataSet = stats[i]
    avg = average(dataSet)
    error = err(dataSet,avg)
    avgs.append(avg)
    errors.append(error)
    print avg
    print error
    print ""
print avgs
print errors
