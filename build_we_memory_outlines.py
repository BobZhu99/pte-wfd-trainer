"""Build the 37-topic bilingual WE memory outlines from simple, curated ideas."""
import json
import sys
from pathlib import Path
from we_expansion_content import build_expansion, render_expanded_markdown

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).parent

# Each topic: whether-clause, although-clause, position, then
# reason / explanation / example / link for each of the two body paragraphs.
# Every line contains English | Chinese. These are illustrative writing examples.
DATA = r"""
@1
city life is better than country life | 城市生活是否比乡村生活好
country life is quiet | 乡村生活很安静
city life is better for me | 城市生活更适合我
city life saves travel time | 城市生活节省出行时间
shops and schools are usually nearby | 商店和学校通常就在附近
I can walk to a shop in five minutes | 我走五分钟就能到商店
this helps me save time | 这帮助我节省时间
it is easier to get medical help in cities | 在城市更容易得到医疗帮助
there are more hospitals nearby | 附近有更多医院
I can reach a hospital quickly when I feel ill | 我不舒服时可以很快到医院
this makes my life easier | 这让我的生活更方便

@2
famous people should give up their privacy | 名人是否应该放弃隐私
fans want to know about their lives | 粉丝想了解他们的生活
famous people should keep their privacy | 名人应该保留隐私
privacy helps them rest | 隐私帮助他们休息
they need quiet time after work | 他们工作后需要安静的时间
a singer can rest at home without cameras outside | 歌手可以在家休息，外面没有相机拍摄
this helps the singer feel less stressed | 这帮助歌手减轻压力
privacy protects their family life | 隐私保护他们的家庭生活
their children also need a normal life | 他们的孩子也需要正常生活
an actor can take a child to school without being followed | 演员可以不被跟拍地送孩子上学
this makes family life easier | 这让家庭生活更轻松

@3
young people should wait until 25 to drive | 年轻人是否应等到25岁才能开车
driving can be dangerous | 开车可能有危险
18 is a suitable age to start driving | 18岁是开始开车的合适年龄
young people need time to learn road safety | 年轻人需要时间学习道路安全
they must understand traffic rules before driving | 他们开车前必须理解交通规则
I took driving lessons at 18 and learned to check my mirrors | 我18岁时上驾驶课，学会查看后视镜
this helped me drive more safely | 这帮助我更安全地开车
driving at 18 makes daily life easier | 18岁可以开车让日常生活更方便
young adults need to travel to school or work | 年轻成年人需要去上学或上班
I drove to college instead of waiting for a bus | 我开车去大学，不用等公交
this helped me save time | 这帮助我节省时间

@4
governments should spend money on old buildings | 政府是否应该花钱保护古建筑
new homes are also needed | 人们也需要新住房
old buildings should be protected, but new homes also need money | 古建筑应该保护，但新住房也需要资金
old buildings help people learn history | 古建筑帮助人们学习历史
people can see how others lived in the past | 人们能看到过去的人怎样生活
I visited an old house and saw an old kitchen | 我参观古老住宅，看到了旧式厨房
this helped me understand life in the past | 这帮助我理解过去的生活
building repairs can leave less money for new homes | 修复建筑可能挤占新住房的资金
governments cannot spend the same money twice | 政府不能把同一笔钱花两次
an expensive repair project may leave no money for new flats | 昂贵的修复工程可能使政府没钱建新公寓
this can make it harder to provide enough homes | 这可能使政府更难提供足够住房

@5
laws can change people's behaviour | 法律是否可以改变人的行为
some people still break laws | 有些人仍然违法
laws can change behaviour | 法律可以改变行为
punishment can stop people from breaking rules | 惩罚可以阻止人们违反规则
people do not want to pay fines | 人们不想交罚款
drivers may slow down when speeding leads to a fine | 超速会被罚款时，司机可能减速
this can make roads safer | 这可以让道路更安全
laws tell people what they must do | 法律告诉人们必须做什么
clear rules make the right action easier to understand | 清楚的规则使人更容易知道该怎么做
drivers stop at red lights because the rule is clear | 司机在红灯时停车，因为规则很清楚
this helps people behave properly | 这帮助人们正确行动

@6
governments should improve public transport rather than build more roads | 政府是否应该优先改善公共交通而不是多修路
more roads can help drivers | 更多道路能帮助司机
public transport should come first | 应该优先改善公共交通
public transport saves people money | 公共交通帮助人们省钱
bus fares can cost less than driving and parking | 公交票价可能比开车和停车的费用低
I spend three dollars on a bus instead of ten dollars on parking | 我花三元坐公交，不用花十元停车
this helps me save money | 这帮助我省钱
public transport can reduce traffic | 公共交通可以减少拥堵
one bus can carry many people | 一辆公交车能载很多人
a full bus can replace many cars | 一辆满载的公交可以代替很多汽车
this can make the roads less crowded | 这可以让道路不那么拥挤

@7
parents should share legal responsibility for their children's actions | 家长是否应为孩子的行为承担部分法律责任
parents cannot watch children all the time | 家长不能一直看着孩子
parents should share responsibility when their young children cause harm | 年幼孩子造成伤害时，家长应分担责任
parents can teach children basic rules | 家长可以教孩子基本规则
young children learn from adults at home | 年幼孩子会向家里的成年人学习
a parent can teach a child not to damage other people's things | 家长可以教孩子不破坏别人的东西
this helps children behave better | 这帮助孩子表现得更好
responsibility makes parents pay more attention | 承担责任让家长更留意
parents may act earlier when they notice a problem | 家长发现问题时可能更早采取行动
a parent can stop a child from throwing stones at windows | 家长可以阻止孩子向窗户扔石头
this helps prevent damage | 这帮助防止损坏

@8
there should be a maximum wage | 是否应该设置最高工资
some people earn much more than others | 有些人的收入远高于其他人
there should not be a maximum wage | 不应该设置最高工资
higher pay can encourage hard work | 更高工资可以鼓励努力工作
people want a reward for doing a good job | 人们希望做好工作能得到回报
a worker may work harder to earn a bonus | 员工可能为得到奖金而更加努力
this can improve the quality of work | 这可以提高工作质量
good pay helps companies keep good workers | 好工资帮助公司留住好员工
workers may leave if they can earn more elsewhere | 如果别处工资更高，员工可能离开
a good cook may stay at a restaurant that pays well | 好厨师可能留在工资高的餐厅
this helps the business run well | 这帮助企业正常运作

@9
shorter working weeks can reduce unemployment | 缩短工作周是否能减少失业
shorter hours do not suit every job | 较短工时并不适合所有工作
shorter working weeks can help some workers but also cause problems | 缩短工作周能帮助部分员工，也会带来问题
sharing work can create more jobs | 分担工作可以创造更多岗位
one person's hours can be shared with another worker | 一个人的工时可以分给另一位员工
a shop can give some hours to a young person looking for work | 商店可以把一些工时分给正在找工作的年轻人
this gives more people a chance to work | 这让更多人有工作的机会
shorter hours can mean lower pay | 工时缩短可能意味着工资降低
some workers are paid by the hour | 有些员工按小时拿工资
an adult working fewer paid hours may find it hard to pay rent | 有的成年人有薪工时减少后，可能难以付房租
this can make daily life harder | 这可能让日常生活更困难

@10
people will work fewer hours in the future | 人们未来是否会工作更少时间
some jobs will still need people | 有些工作仍然需要人
people may work fewer hours in the future | 人们未来可能工作更少时间
computers can save time in offices | 电脑可以节省办公室的工作时间
they can finish simple tasks quickly | 它们可以快速完成简单任务
I use a computer to add numbers instead of doing it by hand | 我用电脑加数字，不用手算
this helps me finish work faster | 这帮助我更快完成工作
machines can do factory work faster | 机器可以更快完成工厂工作
they can repeat the same task many times | 它们可以反复执行同一任务
a machine can pack boxes while workers check the results | 机器装箱，工人检查结果
this may reduce the time workers need | 这可能减少员工所需的时间

@11
building design affects work and daily life | 建筑设计是否影响工作和生活
good buildings can cost more | 好的建筑可能更贵
good building design improves daily life | 好的建筑设计能改善日常生活
good design makes rooms more comfortable | 好的设计让房间更舒适
windows can bring in light and fresh air | 窗户可以带来光线和新鲜空气
I feel better in a bright room with an open window | 在明亮且开窗的房间里，我感觉更好
this makes my home more comfortable | 这让我的家更舒适
quiet rooms help people focus | 安静的房间帮助人们集中注意力
less noise means fewer breaks in their attention | 噪音少，注意力就较少被打断
I finish homework faster in a quiet room | 我在安静的房间做作业更快
this helps me study better | 这帮助我更好地学习

@12
students can work and study at the same time | 学生是否能兼顾工作和学习
working takes time and energy | 工作会花费时间和精力
students can combine study with a small part-time job | 学生可以兼顾学习和少量兼职工作
a short part-time job leaves time for study | 工时较短的兼职能留下学习时间
students do not have to work every day | 学生不必每天上班
I work for a few hours on Saturday and study on weekdays | 我周六工作几小时，平日学习
this helps me keep enough study time | 这帮助我保留足够的学习时间
a simple plan helps students manage both tasks | 简单的计划帮助学生兼顾两件事
they can choose different times for work and study | 他们可以把工作和学习安排在不同时间
I finish homework before my evening shift | 我在晚上上班前完成作业
this helps me avoid missing schoolwork | 这帮助我避免耽误学业

@13
people can keep a good balance between work and life | 人们是否能保持工作和生活的平衡
work is important | 工作很重要
this balance matters but is hard to keep | 这种平衡很重要，但很难保持
time away from work helps people rest | 工作以外的时间帮助人们休息
people need sleep and time to relax | 人们需要睡眠和放松时间
I feel better after a quiet evening at home | 在家度过一个安静的晚上后，我感觉更好
this helps me stay well | 这帮助我保持良好状态
long working hours leave little free time | 长工时使空闲时间很少
people may still have work to finish at night | 人们晚上可能仍有工作要完成
a worker answering emails at home misses a family meal | 员工在家回复邮件，错过了家庭晚餐
this makes work-life balance harder | 这使工作和生活更难平衡

@14
work leaves people too little personal time | 工作是否让人们缺少私人时间
jobs provide money for daily life | 工作提供生活所需的钱
this problem is common and can harm daily life | 这个问题很常见，也会损害日常生活
many people work long hours | 很多人工作时间很长
some jobs require extra work after normal hours | 有些工作需要在正常工时后加班
several people I know often get home late from work | 我认识的几个人经常很晚下班回家
this shows that the problem affects many people | 这表明这个问题影响很多人
little free time harms rest and family life | 空闲时间少会影响休息和家庭生活
people cannot relax or spend enough time with family | 人们不能放松，也没有足够时间陪家人
a tired worker may miss dinner with the children | 疲惫的员工可能错过和孩子一起吃晚餐
this can make family life harder | 这可能让家庭生活更困难

@15
modern media bring both benefits and problems | 现代传媒是否既有好处也有问题
getting information is easier now | 现在获取信息更容易
modern media have both good and bad sides | 现代传媒既有好处也有坏处
media help people learn useful information | 传媒帮助人们了解有用信息
news can reach many people quickly | 新闻能很快传给很多人
I check the weather news before leaving home | 我出门前查看天气新闻
this helps me plan my day | 这帮助我安排一天
false information can confuse people | 错误信息可能误导人们
some stories are shared before anyone checks them | 有些消息未经核实就被传播
someone may change travel plans because of a false train notice | 有人可能因假的列车通知改变出行计划
this can waste people's time | 这可能浪费人们的时间

@16
media influence young people's opinions | 传媒是否影响年轻人的观点
parents and teachers also influence them | 家长和老师也会影响他们
media strongly influence young people | 传媒对年轻人影响很大
news can change what young people think | 新闻可以改变年轻人的想法
it introduces problems they have not seen before | 新闻会介绍他们以前没见过的问题
I cared more about litter after watching a report about dirty beaches | 看过海滩垃圾的报道后，我更在意乱扔垃圾的问题
this changed my view of the problem | 这改变了我对这个问题的看法
advertisements can change buying choices | 广告可以改变购买选择
young people often notice products shown many times | 年轻人常会注意反复出现的产品
I wanted a pair of shoes after seeing the same advertisement | 看过同一个广告后，我想买那双鞋
this shows how media affect daily choices | 这说明传媒怎样影响日常选择

@17
television is useful in daily life | 电视在日常生活中是否有用
watching too much television wastes time | 看太多电视浪费时间
television is useful | 电视是有用的
television helps people learn | 电视帮助人们学习
programmes can explain useful things simply | 节目可以简单地解释有用的东西
I learned to cook a simple meal from a cooking show | 我从烹饪节目学会做一道简单的菜
this helped me learn a useful skill | 这帮助我学会一项有用技能
television helps people relax and feel less alone | 电视帮助人们放松，并减少孤独感
funny shows and friendly voices can make evenings happier | 有趣的节目和亲切的声音能让晚上更愉快
I watch a comedy when I spend an evening alone | 我独自度过晚上时看喜剧
this helps me relax and feel less lonely | 这帮助我放松，并减少孤独感

@18
tourism brings as many problems as benefits to poorer countries | 旅游是否给较贫穷国家带来同样多的利与弊
tourism brings money | 旅游会带来收入
tourism has both clear benefits and serious problems | 旅游既有明显好处，也有严重问题
tourism creates local jobs | 旅游创造当地工作岗位
visitors need food and places to stay | 游客需要食物和住宿
a small hotel can hire local people to clean rooms | 小旅馆可以雇当地人打扫房间
this helps local people earn money | 这帮助当地人赚钱
tourism can damage local places | 旅游可能损害当地环境
too many visitors can leave rubbish behind | 太多游客可能留下垃圾
a popular beach may be covered with empty bottles | 热门海滩可能到处都是空瓶子
this makes the area a worse place to live | 这让当地变得不那么适合居住

@19
companies should focus on their name or on discounts | 公司应该重视品牌还是折扣
discounts can attract buyers quickly | 折扣能快速吸引买家
companies should focus more on a trusted name | 公司应该更重视可信的品牌
a trusted name makes buying easier | 可信的品牌让购买更容易
people worry less about the quality | 人们较少担心质量
I buy the same brand of milk because I know its quality | 我买同一个牌子的牛奶，因为我了解它的质量
this helps me choose quickly | 这帮助我快速选择
good quality brings customers back | 好质量会让顾客再次购买
a useful product gives people a reason to buy again | 好用的产品让人有再次购买的理由
I buy the same shoes again because the first pair lasted well | 第一双鞋很耐穿，所以我又买了同款
this helps the company keep customers | 这帮助公司留住顾客

@20
employees should help make company decisions | 员工是否应该参与公司决策
managers have the final responsibility | 经理负最终责任
letting workers help can bring good ideas but take more time | 让员工参与能带来好想法，但会花更多时间
employees can suggest useful ideas | 员工可以提出有用的想法
they deal with daily problems at work | 他们每天处理工作中的实际问题
a shop worker can suggest a clearer place for price signs | 店员可以建议把价格牌放在更清楚的位置
this can make shopping easier | 这可以让购物更方便
more opinions can slow decisions | 更多意见可能让决策变慢
people may disagree and need more discussion | 人们可能不同意，需要更多讨论
a team may spend a whole meeting choosing a new uniform | 团队可能花整场会议选择新制服
this leaves less time for other work | 这让其他工作的时间变少

@21
large shopping malls replacing small shops is a good change | 大商场替代小商店是否是好变化
small shops are useful | 小商店也很有用
shopping malls can improve daily shopping | 商场可以改善日常购物
shopping malls save travel time | 商场节省出行时间
many different shops are in one place | 很多不同商店集中在一起
I buy food and clothes in the same shopping mall | 我在同一个商场买食物和衣服
this helps me finish shopping faster | 这帮助我更快买完东西
shopping malls make prices easier to compare | 商场让价格更容易比较
customers can visit several shops quickly | 顾客可以很快逛几家商店
I compare the price of a shirt in two nearby shops | 我在附近两家店比较一件衬衫的价格
this helps me save money | 这帮助我省钱

@22
governments should take the main responsibility for climate change | 政府是否应对气候变化承担主要责任
companies and individuals should also help | 公司和个人也应该帮忙
governments should take the main responsibility | 政府应该承担主要责任
governments can make rules for everyone | 政府可以制定适用于所有人的规则
one clear rule can guide many companies | 一条清楚的规则可以指导很多公司
a government can tell factories to use cleaner machines | 政府可以要求工厂使用更清洁的机器
this helps many places become cleaner | 这帮助很多地方变得更清洁
governments can pay for better public transport | 政府可以出资改善公共交通
better buses can help more people leave cars at home | 更好的公交可以让更多人不开车
a new bus route can help workers travel without driving | 新公交线路能帮助员工不开车去上班
this can reduce car use | 这可以减少汽车使用

@23
rising temperatures should be a main area of climate study | 气温上升是否应成为气候研究的重点
many climate problems need study | 很多气候问题都需要研究
I would study rising temperatures | 我会研究气温上升
hot weather affects daily life | 炎热天气影响日常生活
people may find it hard to sleep or work | 人们可能难以入睡或工作
I find it hard to sleep on very hot nights | 天气很热的晚上，我难以入睡
this shows why we need ways to deal with heat | 这说明我们为什么需要应对高温的方法
hot weather can damage crops | 炎热天气可能损害庄稼
plants can dry out when there is too much heat | 太热时植物可能干枯
the plants in my garden dried out during a hot week | 一周的高温让我的花园植物干枯了
this shows why heat matters for growing food | 这说明高温为什么会影响粮食种植

@24
air pollution should be a main concern for governments | 空气污染是否应成为政府重点关注的问题
governments face many problems | 政府面临很多问题
air pollution needs urgent action | 空气污染需要尽快处理
air pollution harms people's health | 空气污染损害人们的健康
people need clean air to stay healthy | 人们需要干净空气来保持健康
smoke from cars makes me cough beside a busy road | 在繁忙道路旁，汽车烟雾让我咳嗽
this shows why clean air is important | 这说明干净空气为什么重要
better buses can help reduce air pollution | 更好的公交可以帮助减少空气污染
more people can travel without using their own cars | 更多人可以不开自己的车出行
a frequent bus service helps me leave my car at home | 班次多的公交让我可以把车留在家里
this can help make the air cleaner | 这可以帮助空气变干净

@25
learning languages is still needed when AI can translate | 人工智能可以翻译后，是否仍需要学习外语
AI translation is useful | 人工智能翻译很有用
learning a foreign language is still useful | 学习外语仍然有用
language skills make talking easier | 外语能力让交流更容易
people can speak without checking a phone | 人们不用查看手机就能说话
I order food in English without using a translation app | 我用英语点餐，不用翻译软件
this helps me talk to people faster | 这帮助我更快和别人交流
language skills help people notice translation mistakes | 外语能力帮助人们发现翻译错误
an app may choose the wrong word | 软件可能选错词
I notice that an app gives the wrong meaning for a food name | 我发现软件把一种食物的名称翻译错了
this helps me avoid mistakes | 这帮助我避免错误

@26
smartphones are a useful invention | 智能手机是否是一项有用的发明
phones can distract people | 手机可能让人分心
smartphones improve daily life | 智能手机改善日常生活
smartphones make contact easier | 智能手机让联系更容易
people can call others wherever they are | 人们在不同地点都可以联系别人
I call my family when I am away from home | 我离家时给家人打电话
this helps me stay close to my family | 这帮助我与家人保持联系
smartphones help people find their way | 智能手机帮助人们找路
map apps show where to go | 地图软件会显示路线
I use a map app to find a new shop | 我用地图软件找一家新商店
this helps me save time | 这帮助我节省时间

@27
longer lives made possible by medical technology are a good thing | 医疗技术延长寿命是否是好事
medical care can cost a lot | 医疗可能很贵
longer lives are a good thing | 寿命延长是好事
medical care gives people more years to live | 医疗让人们有更多时间生活
doctors can treat more illnesses | 医生可以治疗更多疾病
a person can recover after treatment and return home | 一个人可以在治疗后康复回家
this gives the person more time to enjoy life | 这让这个人有更多时间享受生活
longer lives give families more time together | 寿命延长让家人有更多相处时间
older people can spend more years with younger family members | 老人可以多陪伴年轻家人几年
a grandfather can watch his grandchildren grow up | 爷爷可以看着孙辈长大
this can make family life happier | 这可以让家庭生活更幸福

@28
children's lives are harder today than in the past | 现在孩子的生活是否比过去更难
children have more useful technology now | 现在的孩子有更多有用的技术
children face more pressure today | 现在的孩子面临更多压力
schoolwork can take up much of their time | 学业可能占据他们很多时间
children may have homework and extra classes | 孩子可能既有作业又有补习课
a child may finish school and then attend another class | 孩子放学后可能还要再上一节课
this leaves less time to rest | 这使休息时间变少
phones can make it harder to focus | 手机可能让专注变得更难
games and messages can interrupt study | 游戏和消息会打断学习
a child keeps checking messages while doing homework | 孩子做作业时不断看消息
this makes schoolwork take longer | 这使完成作业所需的时间更长

@29
learning by doing is useful at school | 在学校通过实践学习是否有用
books are also useful | 书本也有用
learning by doing helps students learn | 实践帮助学生学习
doing a task makes it easier to remember | 亲手做一件事让人更容易记住
students connect an idea with a real action | 学生把知识与实际行动联系起来
I grew a plant in class and remembered that it needed water | 我在课堂上种植物，记住了植物需要水
this helped me remember the lesson | 这帮助我记住课堂内容
practice builds useful skills | 练习培养有用技能
students learn to complete tasks themselves | 学生学会自己完成任务
I learned to cook by making a simple meal | 我通过做一道简单的菜学会做饭
this helped me do the task by myself | 这帮助我自己完成这件事

@30
travel is necessary for a good education | 旅行是否是良好教育的必要条件
travel can teach useful things | 旅行能教人有用的东西
a good education does not require travel | 获得良好教育并不一定需要旅行
students can learn well at local schools | 学生可以在本地学校学得很好
local teachers can explain the same basic subjects | 本地老师也能讲解相同的基础科目
I learned maths at a school near my home | 我在家附近的学校学习数学
this shows that learning does not require travel | 这说明学习不一定需要旅行
online lessons bring learning to people's homes | 网络课程把学习带到人们家里
students can watch teachers from other places | 学生能观看其他地方老师的课程
I watch an English lesson online at home | 我在家上网看英语课
this helps me learn without leaving home | 这帮助我足不出户地学习

@31
written exams are a useful way to test learning | 笔试是否是检验学习的有效方式
presentations can also be useful | 演讲展示也有用
written exams are useful | 笔试有用
exams show what students understand | 考试显示学生理解了什么
students must answer questions by themselves | 学生必须独立答题
I remembered a maths formula but could not use it in an exam | 我记得一个数学公式，但考试时不会运用
this showed that I needed more practice | 这说明我需要更多练习
exam results help students plan their study | 考试结果帮助学生安排学习
wrong answers show what needs more work | 错误答案显示哪些地方需要加强
I reviewed the questions I got wrong after an exam | 考试后我复习了做错的题
this helped me improve my learning | 这帮助我改进学习

@32
universities should take marks off for late work | 大学是否应该对迟交作业扣分
students can have real problems | 学生可能遇到实际困难
schools should take off a few marks, but give extra time for real problems | 学校应该扣少量分数，但实际困难应允许延期
deadlines should be fair to all students | 截止日期应对所有学生公平
students who finish on time should not be treated worse | 按时完成的学生不应受到不利对待
I submit work on time while another student asks for extra days without a reason | 我按时交作业，另一名学生却无理由要求多几天
taking off a few marks helps keep the rules fair | 扣少量分数帮助规则保持公平
schools should allow extra time for real problems | 学校应为实际困难允许延期
illness can stop students from finishing work | 生病可能使学生无法完成作业
a student in hospital may need a few extra days | 住院的学生可能需要多几天
this helps students finish work without unfair punishment | 这帮助学生完成作业，避免不公平的惩罚

@33
universities should replace paper books with digital books | 大学是否应该用电子书替代纸质书
digital books are useful | 电子书有用
universities should use digital books but keep some paper books | 大学应该用电子书，但也保留一些纸质书
digital books can save printing costs | 电子书可以节省印刷费用
the same file can be used without printing more pages | 同一个文件可以重复使用，不必多印纸张
I read class notes on a screen instead of printing them | 我在屏幕上读课堂笔记，不把它们打印出来
this helps save paper and money | 这帮助节省纸张和金钱
digital books are hard to use without a working device | 没有能用的设备时，电子书很难使用
students need a phone or computer with enough power | 学生需要有电的手机或电脑
I cannot read an electronic book when my phone battery is dead | 手机没电时，我看不了电子书
keeping paper books gives students another choice | 保留纸质书让学生多一个选择

@34
life experience teaches better than books | 生活经验是否比书本教得更好
books provide useful information | 书本提供有用信息
experience is often a better teacher | 经验通常是更好的老师
personal experience is easier to remember | 亲身经历更容易记住
people remember what happens to them | 人们会记得发生在自己身上的事情
I remember missing a bus because I left home late | 我记得自己因为出门晚而错过公交
this taught me to leave earlier | 这教会我早点出门
experience helps people solve real problems | 经验帮助人们解决实际问题
people learn by trying a task themselves | 人们通过亲自尝试来学习
I learned to cook by making a simple meal | 我通过做一道简单的菜学会做饭
this helped me do the task by myself | 这帮助我自己完成这件事

@35
students should study plays written long ago | 学生是否应该学习很久以前写的戏剧
old plays can be difficult | 古老戏剧可能很难
old plays can be useful, but students need help | 古老戏剧可能有用，但学生需要帮助
old plays help students learn about the past | 古老戏剧帮助学生了解过去
stories show old ways of living | 故事会展示过去的生活方式
I read a play that showed how families lived long ago | 我读过一部展示过去家庭生活的戏剧
this helped me understand history | 这帮助我理解历史
old language can be hard to understand | 古老的语言可能很难理解
some words are not used in daily life today | 有些词现在日常生活中不用了
I needed my teacher to explain several old words | 我需要老师解释几个古老的词
simple notes can make the play easier to read | 简单的注释可以让戏剧更容易读懂

@36
media shape people's views and behaviour | 传媒是否塑造人们的观点和行为
people can think for themselves | 人们可以独立思考
media influence both views and behaviour | 传媒既影响观点也影响行为
news changes how people see problems | 新闻改变人们看待问题的方式
it gives people information they did not have before | 新闻提供人们以前不知道的信息
I cared more about litter after watching a report about dirty beaches | 看过海滩垃圾的报道后，我更在意乱扔垃圾的问题
this changed my view of the problem | 这改变了我对这个问题的看法
programmes can encourage new habits | 节目可以鼓励新的习惯
people may copy useful actions they see | 人们可能模仿看到的有用行为
I started using a shopping bag again after watching a programme about waste | 看过关于垃圾的节目后，我开始重复使用购物袋
this helped me change a daily habit | 这帮助我改变一个日常习惯

@37
all students should learn a foreign language | 是否所有学生都应该学习外语
learning a language takes time | 学习一门语言需要时间
schools should require students to learn a foreign language | 学校应该要求学生学习外语
language skills make travel easier | 外语能力让旅行更方便
travellers can ask for help directly | 旅行者可以直接求助
I use English to ask where the bus stop is | 我用英语询问公交站在哪里
this helps me find my way | 这帮助我找到路
language skills can help at work | 外语能力可以在工作中帮忙
workers may need to speak to foreign customers | 员工可能需要与外国顾客交流
a shop worker uses English to help a visitor buy a ticket | 店员用英语帮助游客买票
this helps the worker serve more customers | 这帮助员工接待更多顾客
"""

FIELDS = ['topic', 'although', 'position', 'r1', 'x1', 'e1', 'c1', 'r2', 'x2', 'e2', 'c2']

NOTES = {
    3: '开车统一选18岁。问25岁限制，就说不必等到25岁；问最低年龄，就明确回答18岁。',
    4: '第二段是保护古建筑的好处，第三段是资金取舍的坏处；问到住房时，用第三段回应住房。',
    9: '一利一弊。年轻人可用分工得到岗位，成年人可能因收入下降而受影响；立场是适用于部分工作，并非所有人。',
    13: '第二段回答“为什么重要”，第三段回答“为什么难”。不要把第三段写成第二个好处。',
    14: '第二段回答“有多普遍”，第三段回答“有什么后果”。',
    15: '一利一弊：得到信息更快，也可能被错误信息误导。',
    17: '理由一覆盖学习；理由二同时覆盖放松和陪伴。',
    18: '一利一弊。采取折中观点：就业收入是好处，环境破坏是坏处，很难说只有一面。',
    20: '一利一弊：想法更实用，但讨论可能拖慢决定。',
    22: '主要责任选政府；Although保留公司与个人也需要帮助这一点。',
    23: '研究方向固定选气温上升，不要中途换成另一个方向。',
    24: '第二段解释为什么是严重问题，第三段给出改善公交的解决办法。',
    26: '新发明固定选智能手机，两个好处固定为联系家人和找路。',
    30: '问旅行必要性：不必旅行也能学好；问留学被高估：不必出国也能学好。两个理由共用。',
    32: '第二段表达扣分观点，第三段给出允许合理延期的建议。',
    33: '第二段是电子书的好处，第三段是电子书的局限。结论保留纸质书，不能说完全替代。',
    35: '第二段写好处，第三段写困难和简单办法。',
}


def sentence(text):
    return text[0].upper() + text[1:] + ('' if text.endswith(('.', '?', '!')) else '.')


def make_outlines(bank):
    sections = DATA.strip().split('\n\n')
    result = []
    for section in sections:
        lines = section.splitlines()
        index = int(lines[0][1:])
        assert len(lines[1:]) == len(FIELDS), (index, len(lines))
        item = bank[index - 1]
        assert item['index'] == index
        values = {}
        for key, line in zip(FIELDS, lines[1:]):
            en, zh = line.split(' | ', 1)
            values[key] = {'en': en, 'zh': zh}
        v = values
        opening_en = (f"Whether {v['topic']['en']} has been widely discussed. "
                      f"Although {v['although']['en']}, I believe {v['position']['en']} "
                      f"because {v['r1']['en']} and {v['r2']['en']}.")
        opening_zh = (f"关于“{v['topic']['zh']}”已有很多讨论。虽然{v['although']['zh']}，"
                      f"但我认为{v['position']['zh']}，因为{v['r1']['zh']}，而且{v['r2']['zh']}。")
        closing_en = (f"In conclusion, I believe {v['position']['en']} "
                      f"because {v['r1']['en']} and {v['r2']['en']}.")
        closing_zh = (f"总之，我认为{v['position']['zh']}，因为{v['r1']['zh']}，"
                      f"而且{v['r2']['zh']}。")
        bodies = []
        for number, transition in [(1, 'First'), (2, 'Second')]:
            n = str(number)
            bodies.append([
                {'label': '理由' if index not in (13, 14, 24, 32) else '本段重点',
                 'en': f"{transition}, {v['r' + n]['en']}.", 'zh': v['r' + n]['zh'] + '。'},
                {'label': '解释', 'en': f"This is because {v['x' + n]['en']}.", 'zh': '这是因为' + v['x' + n]['zh'] + '。'},
                {'label': '例子', 'en': f"For example, {v['e' + n]['en']}.", 'zh': '例如，' + v['e' + n]['zh'] + '。'},
                {'label': '回扣', 'en': sentence(v['c' + n]['en']), 'zh': v['c' + n]['zh'] + '。'},
            ])
        result.append({
            'index': index, 'qid': item['qid'], 'qids': item['qids'],
            'title': item['title'].strip(), 'title_en': item['title_en'],
            'question': {'en': item['prompt'], 'zh': item['prompt_zh']},
            'question_variants': item.get('prompt_variants', []),
            'question_source': item['prompt_source'], 'values': values,
            'opening': {'en': opening_en, 'zh': opening_zh},
            'body1': bodies[0], 'body2': bodies[1],
            'closing': {'en': closing_en, 'zh': closing_zh},
            'note': NOTES.get(index, ''),
        })
        result[-1]['expanded'] = build_expansion(result[-1])
    assert len(result) == len(bank) == 37
    assert [item['index'] for item in result] == list(range(1, 38))
    return result


def render_markdown(outlines):
    lines = [
        '# WE 37题：极简双语记忆提纲', '',
        '这是一份记忆提纲，不是200–300词的完整考场作文。每题固定四段，用最简单的常识、熟词和日常例子。', '',
        '**例子全部已经配好，均为写作示例，可以直接用来记忆句式和思路，不需要另外编例子。**', '',
        '固定结构：Whether → Although → I believe → because 1 and 2；两段主体各用“理由—解释—例子—回扣”；结尾重复观点和两个要点。', '',
        '**Whether** 是正确拼写。理由可以重复熟词，例子可以重复常见场景。利弊题的一段写好处、一段写坏处；原因、问题、建议题只调整段落任务。', '',
        '## 题目目录', '', '| 序号 | 中文题目 | 英文题目 | 机构题号 |', '|---|---|---|---|',
    ]
    for o in outlines:
        lines.append(f"| {o['index']} | {o['title']} | {o['title_en']} | {' / '.join(o['qids'])} |")
    for o in outlines:
        v = o['values']
        lines += [
            '', '---', '', f"## {o['index']:02d}. {o['title']}", '',
            '**英文标题：** ' + o['title_en'], '',
            '**题号：** ' + ' / '.join('#' + qid for qid in o['qids']), '',
            '### 英文原题与中文释义', '', o['question']['en'], '', o['question']['zh'], '',
            '英文原文来源：萤火虫题库《WE.pdf》，PDF第' + '、'.join(str(p) for p in o['question_source']['pages']) + '页。', '',
        ]
        for variant in o['question_variants']:
            lines += ['**另一种英文问法：**', '', variant['en'], '', variant['zh'], '']
        lines += [
            f"**只记三点：** {v['position']['zh']}；①{v['r1']['zh']}；②{v['r2']['zh']}。", '',
        ]
        if o['note']:
            lines += ['**题目提醒：** ' + o['note'], '']
        lines += ['### 第一段：话题＋让步＋观点＋两个要点', '', o['opening']['en'], '', o['opening']['zh'], '']
        for key, heading in [('body1', '第二段：理由一＋解释＋例子＋回扣'), ('body2', '第三段：理由二＋解释＋例子＋回扣')]:
            lines += [f'### {heading}', '']
            for step in o[key]:
                lines += [f"**【{step['label']}】** {step['en']}  ", step['zh'], '']
        lines += ['### 第四段：重申观点＋总结两个要点', '', o['closing']['en'], '', o['closing']['zh'], '']
    return '\n'.join(lines)


if __name__ == '__main__':
    bank = json.loads((ROOT / 'we_questions.json').read_text(encoding='utf-8'))
    outlines = make_outlines(bank)
    (ROOT / 'we_memory_outlines.json').write_text(json.dumps(outlines, ensure_ascii=False, indent=2), encoding='utf-8')
    target = ROOT / 'WE_37题_极简双语记忆提纲.md'
    target.write_text(render_markdown(outlines), encoding='utf-8')
    expanded_target = ROOT / 'WE_37题_简单拓展版_200词.md'
    expanded_target.write_text(render_expanded_markdown(outlines), encoding='utf-8')
    print(f'Created {len(outlines)} bilingual outlines: {target}')
    counts = [o['expanded']['word_count'] for o in outlines]
    print(f'Created {len(outlines)} expanded essays: {min(counts)}–{max(counts)} English words each.')
