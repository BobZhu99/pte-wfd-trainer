"""Simple, topic-specific extra details for the WE memory outlines."""
import itertools
import re

# Two explanation details and one example detail for each body paragraph.
# The builder selects a coherent set that keeps each English essay at 210–225 words.
DATA = r"""
@F101062
People do not need to travel far for simple tasks. They can use that time for other things. | 人们办简单的事情不用走很远，可以把时间用在其他事情上。
This is useful for people who work or study every day and have little free time. | 这对每天工作或学习、空闲时间很少的人很有用。
I can buy what I need and return home quickly. I do not need to wait for a bus. | 我能很快买好需要的东西回家，不用等公交。
When someone feels ill, a long journey can be difficult. A nearby hospital makes getting help easier. | 人不舒服时，长途出行可能很困难，附近的医院让求助更容易。
Families can also visit sick relatives more easily when the hospital is close to their own homes. | 医院离家近时，家人也更容易探望生病的亲人。
My family can take me there and bring me home. We do not spend hours on the road. | 家人可以送我去，再接我回家，不用在路上花几小时。

@F101134
Their work may be public, but their home should still be a quiet place where they can relax. | 他们的工作可能面向公众，但家仍应该是可以安静放松的地方。
Constant attention can make a normal day tiring. Everyone needs a break from work and other people's questions. | 持续受到关注会让普通的一天也很累，每个人都需要暂时离开工作和别人的追问。
The singer can sleep, cook and spend time with friends. These are simple things that everyone needs. | 歌手可以睡觉、做饭、和朋友相处，这些是每个人都需要的普通事情。
Family members did not choose a public job. They should not lose their freedom because someone else is famous. | 家人没有选择面向公众的工作，不应该因为亲人成名而失去自由。
Children should be able to learn and play without strangers watching them or sharing their photos online. | 孩子应该能正常学习和玩耍，而不是被陌生人盯着或把照片传到网上。
The child can enter school quietly and meet friends. A normal school day should not become a public event. | 孩子可以安静地进学校、见朋友，普通的上学日不应该变成公开活动。

@F101136
Before they drive alone, they should learn how to stop, turn and share the road with other people. | 独自开车前，他们应学会停车、转弯，以及和其他人共同使用道路。
A clear age rule can give young people time to prepare. Driving lessons are also needed to keep them safe. | 清楚的年龄规则可以给年轻人准备时间，也需要驾驶课来保障安全。
My teacher asked me to look carefully before moving. I practised this many times until it became a habit. | 老师要求我开动车前认真观察，我练了很多次，直到形成习惯。
Not every family can drive a young adult to every class or job. Being able to travel alone is useful. | 不是每个家庭都能每次接送年轻人上课或上班，能独立出行很有用。
Waiting until 25 could make some young adults depend on their parents for several more years. | 等到25岁可能让部分年轻人多依赖父母好几年。
I could leave home at a suitable time and arrive before class. My parents did not need to take me. | 我能在合适的时间出门，上课前到达，父母不用送我。

@F101138
Books can explain history, but a real building helps people see it. Old rooms make the past easier to imagine. | 书本能解释历史，但真实建筑让人看到历史，旧房间让过去更容易想象。
Schools can take students to these places. A short visit can make a history lesson more interesting and easier to remember. | 学校可以带学生参观，短暂参观能让历史课更有趣、更容易记住。
The kitchen was very different from mine. Seeing it helped me understand how people cooked before modern machines existed. | 那个厨房和我家很不一样，看到它让我理解没有现代机器时人们怎样做饭。
Some families need a safe place to live now. A beautiful old building cannot meet that basic need. | 有些家庭现在就需要安全的住所，一座美丽的古建筑无法满足这一基本需要。
Repair costs can also continue for years. Money is needed again when roofs, walls or windows become damaged. | 修复费用可能持续多年，屋顶、墙壁或窗户损坏时还需要再花钱。
The government may have to delay the housing plan. Families would then wait longer for a suitable place to live. | 政府可能不得不推迟住房计划，家庭就要更久才能等到合适的住所。

@F101003
Without a clear cost, some people may ignore a rule. A fine gives them a reason to stop and think. | 如果没有明确代价，有些人可能无视规则，罚款会让他们停下来考虑。
The rule should be clear and used fairly. People are more likely to follow it when they understand the result. | 规则应清楚并公平执行，人们理解后果时更可能遵守。
A driver may check the speed more often after receiving a fine. The same mistake is then less likely to happen again. | 司机被罚款后可能更常检查车速，同样的错误就较少再次发生。
People share roads and public places. They need common rules so that one person's actions do not hurt others. | 人们共同使用道路和公共场所，需要共同规则，避免一个人的行为伤害别人。
Clear rules can also make daily decisions easier. People do not have to guess what other people will do. | 清楚的规则也让日常决定更容易，人们不用猜别人会怎么做。
Other drivers and people on foot can then cross safely. Everyone knows when to move and when to wait. | 其他司机和行人就能安全通行，大家知道何时走、何时等。

@F101124
Many people travel every day, so even a small saving can add up over a week or a month. | 很多人每天出行，即使每天省一点，一周或一个月下来也能省不少。
People who do not own a car can use the same service. Better transport can help them reach more places. | 没有车的人也能使用同样的服务，更好的交通能帮助他们去更多地方。
I can use the money I save to buy food or pay other bills. This matters to my daily budget. | 我能把省下的钱用来买食物或付账单，这对日常预算很重要。
Building another road does not always remove traffic. More people may simply choose to drive on the new road. | 再修一条路不一定能消除拥堵，可能只是让更多人选择开车上新路。
A useful bus service should be frequent and easy to reach. People need it to fit their daily plans. | 好用的公交应班次多、容易到达，人们需要它配合每天的安排。
If more workers take that bus, there will be fewer cars near the office during the busiest part of the day. | 如果更多员工坐那辆公交，一天最忙时办公室附近的汽车就会减少。

@F101042
Children may not understand the results of their actions. Adults can explain them in simple daily lessons. | 孩子可能不理解行为的后果，成年人可以在日常生活中简单解释。
This does not mean parents can control everything. It means they should make a reasonable effort to guide young children. | 这不意味着家长能控制一切，而是应合理努力去引导年幼孩子。
The parent can ask the child to return a borrowed toy carefully. Small lessons can build better habits over time. | 家长可以要求孩子认真归还借来的玩具，小事能逐渐培养好习惯。
An early warning is often easier to deal with than serious damage later. Parents can set limits before problems grow. | 较早出现的警告往往比后来的严重损坏更容易处理，家长可以提前设限。
Parents should also get help from schools when needed. Children learn better when adults give them the same clear message. | 必要时家长也应向学校求助，成年人传达一致的信息时，孩子更容易学会。
The parent can explain that broken glass may hurt someone. The child can then choose a safer place to play. | 家长可以解释碎玻璃可能伤人，孩子就能换个更安全的地方玩。

@F101140
A person may spend years learning a difficult skill. Better pay can help them feel that their hard work matters. | 一个人可能花多年学习难学的技能，更高工资能让他们觉得努力有价值。
The same wage limit may not suit every job. Different jobs require different levels of skill, time and responsibility. | 同一工资上限可能不适合所有工作，不同工作需要不同的技能、时间和责任。
The worker may serve customers more carefully and finish tasks on time. The business can benefit from this extra effort. | 员工可能更认真服务顾客、按时完成任务，企业也能从额外努力中受益。
Replacing an experienced worker takes time. A new person may need many weeks to learn how the job works. | 更换有经验的员工需要时间，新人可能要花好几周熟悉工作。
Good workers can also teach others. Keeping them can help the whole team learn and do its daily work better. | 好员工也能教别人，留住他们能帮助整个团队学习、做好日常工作。
The restaurant does not need to find a new cook. Customers can continue to enjoy the food they already like. | 餐厅不用再找新厨师，顾客也能继续吃到已经喜欢的食物。

@F101132
The total amount of work may stay the same, but the hours can be divided between more people. | 工作总量可能不变，但工时可以分给更多人。
This may suit jobs with clear shifts. It can give someone a first job and a chance to learn basic skills. | 这可能适合班次清楚的工作，能让人得到第一份工作、学习基本技能。
The young worker can learn to serve customers and follow a daily plan. This experience may help with future work. | 年轻员工能学习服务顾客、遵循日常计划，这种经验可能帮助未来的工作。
Rent, food and transport still cost money each week. Working fewer hours does not make those bills disappear. | 每周仍需付房租、食物和交通费，工时减少不会让账单消失。
The plan may help young people find jobs but worry adults with families. It cannot suit every worker equally. | 这一计划可能帮年轻人找工作，却让有家庭的成年人担心，并不适合同样对待所有人。
The adult may need a second job to cover the missing pay. This could remove the benefit of having fewer hours. | 成年人可能要找第二份工作补收入，工时减少的好处可能因此消失。

@F101135
Many office tasks involve finding information or checking numbers. A simple computer program can complete some of these tasks quickly. | 很多办公室任务是查信息或核对数字，简单电脑程序能快速完成部分任务。
Workers still need to check the results. However, they may not need to spend the whole day on the same task. | 员工仍需检查结果，但可能不用一整天都做同一件事。
I can then spend the saved time on other work. If the whole job takes less time, working hours may fall. | 我可以把省下的时间用在其他工作上，整份工作耗时减少，工时就可能缩短。
Some factory tasks are tiring because workers repeat the same movement all day. Machines can take over part of this work. | 有些工厂任务要整天重复同一动作，很累，机器可以承担其中一部分。
This may also give workers more time to check quality. They can focus on problems that still need human attention. | 这也可能让员工有更多时间检查质量，专注处理仍需要人注意的问题。
Workers can check the packed boxes instead of filling every box themselves. The same amount of work may finish earlier. | 工人可以检查装好的箱子，不必自己装每一箱，同样的工作量可能更早完成。

@F101056
People spend many hours inside buildings. A room that is too dark or hot can make these hours unpleasant. | 人们在建筑里待很久，太暗或太热的房间会让这些时间不舒服。
Small design choices can make a difference. People should be able to open a window and use daylight when possible. | 小的设计选择也能有影响，条件允许时人们应能开窗、利用自然光。
I do not need to keep a strong light on during the day. The room feels more open and pleasant. | 我白天不必一直开很亮的灯，房间感觉更开阔、更舒服。
People often need to read, think or talk at work. Loud noise can make all of these tasks harder. | 人们在工作中常需要阅读、思考或交谈，噪音会让这些事更难。
Separate rooms or better walls can reduce unwanted sound. This helps people continue their work without stopping so often. | 独立房间或更好的墙体能减少噪音，让人工作时不用经常停下来。
I can read a page once and understand it. In a noisy room, I often need to read it again. | 我读一遍就能理解一页内容，在吵闹房间里却常需要再读一次。

@F101044
A part-time job should fit around classes, not replace them. Students need to choose a small number of suitable hours. | 兼职应该配合上课，而不是取代上课，学生应选择少量合适工时。
Students can also say no to extra shifts during busy school weeks. This keeps their main focus on learning. | 学业忙的星期，学生也可以拒绝加班，把主要精力放在学习上。
I still have evenings free for reading and homework. The job does not take away every part of my week. | 我晚上仍能阅读、做作业，兼职不会占掉一周的全部时间。
A plan makes important dates easy to see. Students can notice an exam before accepting an extra work shift. | 计划让重要日期更清楚，学生能在接受额外班次前留意到考试。
Both work and study need regular effort. Doing a little at the right time can prevent a large problem later. | 工作和学习都需要持续努力，在合适时间做一点，可以避免以后出现大问题。
I can go to work knowing that the task is already done. I do not have to rush late at night. | 我知道作业已完成，就能安心上班，不必深夜赶作业。

@F101127
Money is important, but people cannot work well when they are tired all the time. Rest is a basic need. | 钱很重要，但一直疲惫时人们无法做好工作，休息是基本需要。
Free time also allows people to eat properly and see family. These simple activities can support a better daily life. | 空闲时间也让人正常吃饭、陪伴家人，这些小事能改善日常生活。
I sleep at a normal time and feel ready for the next day. I can then pay more attention at work. | 我按时睡觉，为第二天做好准备，工作时就更能集中注意力。
Some people are afraid of losing their jobs. They may accept more work even when they already feel tired. | 有些人担心丢掉工作，即使已经累了，也可能继续接受更多工作。
Phones can also bring work into the home. It becomes difficult to know when the working day has really ended. | 手机也会把工作带回家，让人难以知道工作日何时才真正结束。
The family may already be eating while the worker is still on the phone. Time together becomes shorter each evening. | 员工仍在打电话时，家人可能已经吃饭了，每晚相处的时间就变短。

@F101126
This happens in many ordinary jobs, not only in highly paid positions. Shops, offices and other workplaces can all have long hours. | 这不只发生在高薪岗位，商店、办公室等普通工作也可能工时很长。
Travel time can make the problem worse. A long trip home takes away more time at the end of the day. | 通勤时间会加重问题，下班后长时间回家，又占掉更多时间。
They often have time only to eat and sleep before working again. This pattern can continue through the whole week. | 他们常常只来得及吃饭、睡觉，就又要工作，这种模式可能持续一整周。
Children and other family members need attention, not only money. A short conversation can be difficult when someone is always busy. | 孩子和家人需要的不只是钱，还有陪伴，一直很忙时连简短交谈都很难。
Without enough rest, people may also get angry more easily. Small problems at home can then lead to arguments. | 休息不足也可能让人更容易生气，家里的小问题就可能引起争吵。
The children may want to talk about school, but the parent is too tired to listen. Both sides can feel unhappy. | 孩子可能想说学校的事，但家长累得听不进去，双方都可能不开心。

@F101009
People no longer need to wait for a newspaper to learn what is happening. Useful news can arrive on a phone. | 人们不必等报纸就能知道发生了什么，有用新闻可以直接传到手机上。
This can help with simple daily decisions, such as when to leave home and which road or train to take. | 这能帮助人们决定何时出门、走哪条路或坐哪趟车等日常小事。
If rain is expected, I take an umbrella and leave a little earlier. This can prevent trouble later in the day. | 如果预报有雨，我会带伞、早点出门，避免之后遇到麻烦。
A message can look true even when it is wrong. People may share it quickly because they want to help others. | 错误消息也可能看起来很真，人们想帮别人，就可能很快转发。
The problem grows when many people repeat the same story. Readers should check an important message before acting on it. | 很多人重复同一消息会加重问题，读者行动前应核实重要信息。
The person may pay for a taxi when the train is actually running. A false message can therefore cost money too. | 列车实际正常运行时，那个人却可能花钱打车，所以错误消息也会让人多花钱。

@F101011
Young people may not have much direct experience of a social problem. A clear report can help them understand it. | 年轻人可能没有亲身经历过某个社会问题，清楚的报道能帮助他们理解。
What they see repeatedly can seem especially important. The choice of news stories can therefore shape what they pay attention to. | 反复看到的事情可能显得特别重要，新闻选题因此会影响他们关注什么。
Before the report, I did not think much about a dropped bottle. Afterwards, I noticed rubbish whenever I visited a beach. | 看报道前，我不太在意一个被丢下的瓶子；后来去海滩时，我总会留意垃圾。
Advertisements often connect a product with a happy or popular person. Viewers may then want the same product for themselves. | 广告常把产品和快乐或受欢迎的人联系起来，观众就可能也想要那个产品。
This does not mean every young person copies an advertisement. It means repeated messages can affect even a small buying decision. | 这不代表每个年轻人都照着广告买，而是反复的信息可能影响小小的购买决定。
I looked for those shoes in a shop even though my old pair still worked. The advertisement had changed what I wanted. | 旧鞋还能穿，我却去店里找那双鞋，广告已经改变了我想要的东西。

@F101013
Watching someone complete a task can make the steps clear. People can then try the same simple steps at home. | 看别人完成任务能让步骤更清楚，人们之后可以在家照着做。
Television can bring useful lessons to people who are not at school. Learning can happen during an ordinary evening at home. | 电视也能让不上学的人学到东西，普通的居家夜晚就能学习。
I watched the cook prepare the food and followed the steps in my own kitchen. My meal turned out well. | 我看厨师准备食物，再在自家厨房照着步骤做，做出来的饭不错。
An empty home can feel very quiet after a long day. A familiar programme can make that time more pleasant. | 忙了一天后，空房子可能显得很安静，熟悉的节目能让那段时间更愉快。
People should still make time for friends and family. Television can help during the times when nobody else is there. | 人们仍应留时间给朋友和家人，电视则能在身边没人时提供陪伴。
The jokes make me laugh, and the voices make the room feel less empty. I feel calmer before going to bed. | 笑话让我发笑，节目中的声音让房间不那么空，睡前我也更平静。

@F101007
These jobs may not require many years of training. Local people can earn an income while learning useful skills at work. | 这些工作可能不需要多年培训，当地人能一边赚钱一边学习有用技能。
Visitors also buy food and other products from local shops. Their spending can help several small businesses in the same area. | 游客也会在当地商店买食物和其他东西，消费能帮助同一地区的多家小企业。
The hotel worker can use the pay to buy food and support the family. This is a clear benefit of tourism. | 旅馆员工能用工资买食物、养家，这就是旅游业的明显好处。
Smaller towns may not have enough bins or cleaners for a sudden rise in visitors. Rubbish can quickly become a problem. | 小镇可能没有足够垃圾桶和清洁工应对突然增多的游客，垃圾很快就会成为问题。
The same beaches and streets are also used by local families. Tourism should not make these places worse for them. | 当地家庭也使用同样的海滩和街道，旅游不应该让这些地方变差。
Local people may have to clean up after the visitors leave. This takes time and money away from other needs. | 游客离开后，当地人可能需要清理垃圾，花掉本可用于其他需要的时间和钱。

@F101015
A low price may attract someone once, but trust can guide the next purchase. People want products that work as expected. | 低价可能吸引人买一次，但信任会影响下次购买，人们希望产品符合预期。
This matters for daily products that people buy again and again. A reliable choice can remove worry from a small task. | 这对反复购买的日用品很重要，可靠的选择能减少日常小事中的担心。
I do not need to compare every bottle on the shelf. I already know which one my family likes to drink. | 我不用比较货架上每一瓶牛奶，因为已经知道家人喜欢哪一种。
A discount ends after a short time. The quality of the product is still important when the usual price returns. | 折扣过一阵就结束，恢复正常价格后，产品质量仍然重要。
Happy customers may also tell friends about a good product. This can bring the company new customers without another large discount. | 满意的顾客也可能向朋友推荐好产品，公司不用再大打折也能得到新顾客。
The shoes fit well and are comfortable every day. I care more about that than a small saving on an unknown pair. | 那双鞋合脚、每天穿都舒服，我更在意这些，而不是买陌生款式时省下的一点钱。

@F101004
People doing a task every day often notice small problems first. A manager may not see the same problems from an office. | 每天做某项工作的员工常会先发现小问题，坐办公室的经理不一定看得到。
Listening does not mean accepting every suggestion. Managers can choose the ideas that are useful and explain their final decision clearly. | 听取意见不等于接受每条建议，经理可以选有用的想法，并清楚解释最后决定。
Customers can then find the price without asking for help. The worker also has fewer simple questions to answer each day. | 顾客不用求助就能找到价格，员工每天也少答一些简单问题。
A decision sometimes needs to be made quickly. Long meetings can prevent the team from dealing with a real problem in time. | 有时需要快速决定，长会议可能让团队无法及时处理实际问题。
It is useful to set a clear time limit for discussion. This allows people to speak without delaying every other task. | 给讨论设定明确时限很有用，既让人发言，又不拖延其他所有任务。
The team still has customers to serve after the meeting. Spending too long on one small choice can hold up the day. | 开完会后，团队仍要服务顾客，在小选择上花太久会耽误一天的工作。

@F101030
Going to several separate places can take a long time. Having shops together makes a simple shopping trip easier to plan. | 去几个分散的地方可能很费时间，商店集中在一起让购物更容易安排。
People with limited free time can finish several tasks in one visit. They do not need another trip on a different day. | 空闲时间少的人能一次办好几件事，不用改天再跑一趟。
I can finish both jobs before returning home. I do not need to drive across town just to buy another item. | 我能买完两样东西再回家，不用为了另一件东西开车穿过城区。
Seeing prices side by side helps people make a clear choice. They can also check the quality before spending their money. | 一起比较价格有助于清楚选择，人们花钱前也能检查质量。
This is useful when several shops sell similar things. Customers can choose the item that best fits their needs and budget. | 几家商店卖类似东西时，这很有用，顾客可以按需要和预算来选。
If the shirts look equally good, I can choose the cheaper one. The saved money can be used for something else. | 如果两件衬衫看起来一样好，我就买便宜的，把省下的钱用在其他地方。

@F101012
Individual action is useful, but one person cannot set standards for a whole country. Governments have a much wider role. | 个人行动有用，但一个人不能给整个国家定标准，政府的作用范围更大。
Companies also need the same clear rules. This can prevent careful businesses from being treated worse than those that ignore pollution. | 公司也需要相同的清楚规则，避免认真减少污染的企业反而不如不管污染的企业。
Factories would know what changes they need to make. Regular checks could then show whether they are following the rule. | 工厂会知道要做哪些改变，定期检查则能看出它们是否遵守规则。
Large transport projects need planning and money. Many individuals cannot pay for a bus network or build one by themselves. | 大型交通项目需要规划和资金，个人无法独自出资建设公交网络。
Better services should reach the places where people live and work. Buses that are hard to use will not help much. | 更好的服务应到达人们居住和工作的地方，不好用的公交用处不大。
Workers can use the bus every day if it arrives on time. Small daily changes can add up across a city. | 公交准点时，员工可以每天乘坐，全城每天的小改变能逐渐产生影响。

@F101016
Sleep and work are part of everyone's daily life. Studying heat can help people plan safer and more comfortable homes. | 睡眠和工作是每个人的日常生活，研究高温能帮助规划更安全、舒适的住宅。
Simple changes such as shade and better airflow may help. Research can show which changes work best in different places. | 遮阳和更通风等简单改变可能有用，研究能找出不同地方更有效的办法。
I feel tired the next morning and find it harder to focus. A cooler room would make the night easier. | 第二天早上我觉得累、更难专注，凉快的房间能让夜晚更好过。
Food comes from plants that need suitable conditions to grow. Long hot periods can make it harder to produce enough food. | 食物来自需要合适条件才能生长的植物，长时间高温可能让足量生产粮食更难。
Farmers need to know when crops need more water or shade. Better information can help them prepare before serious damage happens. | 农民需要知道何时多浇水或遮阳，更好的信息能帮助他们在严重损害前准备。
I had to water them more often and move some pots into the shade. This small experience made the issue clear. | 我不得不更常浇水，把一些花盆搬到阴凉处，这个小经历让我明白了问题。

@F101055
It affects people when they travel, work or play outside. Clean air is a basic need that many activities depend on. | 人们出行、工作或户外玩耍时都会受影响，很多活动都需要干净空气。
Children and older people also use the same streets. A clean environment should be available to everyone, not only a few people. | 孩子和老人也使用同样的街道，干净环境应属于所有人，而不只是少数人。
I choose a quieter road when I can, but not everyone has that choice. The problem needs wider action than this. | 可以时我会换条安静的路，但不是每个人都能选择，问题需要更大范围的行动。
Governments can add routes and make services more regular. A bus must be useful before people will change their travel habits. | 政府可以增加线路和班次，公交好用后，人们才会改变出行习惯。
Factories should also be checked, and streets should be easier to walk along. Several simple actions can support the same goal. | 也应检查工厂、改善步行道路，几种简单行动可以服务同一个目标。
I can get to work without paying for parking. If others do the same, there will be fewer cars producing smoke. | 我上班不用付停车费，别人也这样做时，排烟的汽车就会减少。

@F101143
A conversation can move quickly. Stopping to type every sentence into an app can make a simple talk slow and awkward. | 对话可能很快，每句话都停下来输入软件，会让简单交流变慢、变尴尬。
Language skills also help when a phone is out of power. People still need to explain what they want clearly. | 手机没电时，外语能力也有用，人们仍需要清楚说明想要什么。
I can answer the worker's questions and ask about the price. I do not have to pass my phone back and forth. | 我能回答店员的问题、询问价格，不必来回递手机。
The meaning of a word can change with the situation. A person who knows the language can check whether the message fits. | 一个词的意思可能随情境变化，懂语言的人能检查表达是否合适。
This does not mean translation tools are useless. They are helpful tools, but people should not depend on them for every word. | 这不代表翻译工具没有用，它们很有帮助，但人们不应每个词都依赖它们。
I can ask the worker to explain the dish in simple words. This helps me choose the food I actually want. | 我可以请店员用简单的话解释菜品，从而选到真正想要的食物。

@F101128
People may live far from their parents or friends. A phone allows a short conversation without a long and expensive journey. | 人们可能住得离父母或朋友很远，手机让人不用长途花钱旅行就能简短交谈。
They can also send a message when they are busy. Keeping in touch becomes part of an ordinary day, not a difficult task. | 忙的时候也能发消息，保持联系成为日常小事，而不是难完成的任务。
I can tell them that I arrived safely and ask about their day. This makes the distance between us feel smaller. | 我可以报平安、问问他们今天怎样，彼此的距离感觉就小了。
Finding a new place can be stressful when the roads are unfamiliar. A map shows the route step by step on the screen. | 不熟悉道路时，找新地方可能很紧张，地图能在屏幕上一步步显示路线。
People can check the route before leaving home and change it if needed. This helps them plan their day more easily. | 人们出门前能查看路线，必要时更改，更容易安排一天。
The app shows where I should turn and how far I still need to go. I do not waste time walking in circles. | 软件告诉我该在哪里转弯、还要走多远，我不用绕圈浪费时间。

@F101039
More time means more chances to do ordinary things. People can continue learning, working or enjoying time with people they love. | 更多时间意味着能多做普通事情，人们能继续学习、工作，或陪伴所爱的人。
The aim should also be a better life, not only a longer one. Care and support still matter after treatment ends. | 目标不应只是活得更久，也应过得更好，治疗结束后仍需要照顾和支持。
The person may return to a job or enjoy a meal at home. These small parts of life can mean a lot. | 那个人可能重返工作、在家吃饭，这些生活小事也很重要。
Family memories take time to build. Extra years can allow people to share birthdays, school events and simple daily conversations. | 家庭回忆需要时间积累，多活几年能让人一起过生日、参加学校活动、日常聊天。
Older people can also share what they know. Advice about work, study and family life can be useful to younger people. | 老人也能分享经验，关于工作、学习、家庭生活的建议能帮助年轻人。
He can listen to their stories and help them with small problems. The whole family can benefit from this time together. | 他能听他们讲故事、帮忙解决小问题，整个家庭都能从相处时间中受益。

@F101139
Finishing one task does not always mean the day is over. Another lesson or test may already be waiting for the child. | 完成一项任务不一定代表一天结束了，孩子可能还有下一节课或考试。
Parents want children to do well, but a full daily plan can leave little space for play or simple family time. | 家长希望孩子表现好，但排满的日程可能挤掉玩耍和陪家人的时间。
By the time the child gets home, it may already be late. Homework then takes up the rest of the evening. | 孩子到家时可能已经很晚，作业又占掉剩下的晚上时间。
Adults may find it difficult to ignore a phone, and children can find it even harder. Messages arrive during quiet study time. | 成年人可能都难以忽略手机，孩子更难，消息会在安静学习时不断到来。
Young people also see other people's lives online. This can make them worry about being less popular or less successful. | 年轻人还会在网上看到别人的生活，担心自己不够受欢迎或不够成功。
The child loses the place on the page and has to start again. A simple task can become a long one. | 孩子忘了刚才读到哪里，不得不重来，简单任务也会拖很久。

@F101040
A sentence in a book can be easy to forget. Doing the task gives students a real event to think about later. | 书里的一句话可能容易忘，亲手做过后，学生以后能回想起真实的事。
Teachers can still explain the main idea first. Practice then gives students a simple way to check whether they understood it. | 老师仍可以先讲主要知识，再通过实践让学生检查自己是否理解。
When the soil became dry, I added water and watched the plant improve. The lesson was connected to something I could see. | 土干后，我浇水并看到植物状态变好，知识和看得见的东西联系起来了。
Knowing the words for a task is not always enough. Students also need to practise the steps in the right order. | 只知道任务相关的词语不一定够，学生还要练习按正确顺序操作。
Small classroom tasks can build confidence before students face a larger task. Mistakes can be corrected while a teacher is nearby. | 课堂小任务可以让学生在做大任务前建立信心，老师在旁时也能及时纠错。
I measured the food, followed the steps and checked the result. Reading a recipe alone would not give me the same practice. | 我量好食物、按步骤做、检查结果，光读食谱不会有同样的练习。

@F101006
A good teacher and regular practice can help students make progress in many subjects. These things can be found near home. | 好老师和持续练习能帮助学生在很多科目上进步，这些在家附近也能找到。
Travel may add useful experience, but it is not the same as learning well. Students still need effort wherever they live. | 旅行可能增加有用经历，但不等于学得好，无论住哪里学生都要努力。
My teacher explained the steps and gave me exercises. I could ask questions without leaving my home town. | 老师解释步骤、布置练习，我不用离开家乡也能提问。
Many lessons can be watched more than once. Students can stop a video, write notes and return to a difficult part. | 很多课程可以反复看，学生能暂停视频、记笔记，再看难的部分。
This can be useful for people who cannot afford travel. A smaller budget should not stop them from receiving a good education. | 这对负担不起旅行的人很有用，预算少不应该让他们无法获得良好教育。
I repeat useful sentences and practise them after the video. The main learning comes from practice rather than from changing my location. | 我重复有用句子，看完视频再练习，主要收获来自练习，而不是换了地方。

@F101005
Remembering a sentence from a book is different from using the idea. A well-chosen question can show the difference clearly. | 记住书里一句话和会运用知识不同，一道选得好的题能清楚显示区别。
Teachers can then see which topics need another explanation. The exam should cover what students actually learned in class. | 老师就能知道哪些知识要再讲一次，考试应覆盖课堂实际学过的内容。
The question used the formula in a new situation. I realised that knowing its name was not enough to solve the problem. | 题目把公式用在新情境中，我意识到只知道公式名称并不足以解题。
Students have limited study time, so they need to choose what to review. Clear feedback can make that choice easier. | 学生学习时间有限，需要选择复习什么，清楚的反馈能让选择更容易。
A mark alone is not enough. Students should also understand why an answer is wrong and how to correct it. | 只有分数还不够，学生也应理解答案为什么错、该怎样改。
I asked my teacher for help and tried similar questions again. I could then spend less time repeating things I already understood. | 我请老师帮忙，又做类似题，就不用一直重复已经懂的内容。

@F101043
A shared deadline gives students the same amount of time. Extra days without a reason can give one person an unfair advantage. | 同一截止日期让学生有同样多的时间，无理由多几天会带来不公平优势。
The rule should be explained before the task starts. Students need to know the date and what happens if they are late. | 任务开始前应解释规则，学生要知道日期以及迟交后果。
The extra time could allow that student to improve the work further. This would not be fair to students who followed the rule. | 额外时间可能让那个学生进一步完善作业，对遵守规则的人并不公平。
The school should ask for a clear reason and agree on a new date. This keeps the system fair and practical. | 学校应了解明确原因、商定新日期，让制度既公平又实际。
A small delay caused by illness is different from simply forgetting a task. Teachers should consider the situation before taking marks off. | 生病导致的小延误和单纯忘记作业不同，老师扣分前应考虑情况。
The student can send a message to the teacher and explain the problem. A clear new deadline gives a fair chance to finish. | 学生可以给老师发消息解释问题，明确的新截止日期让其有公平的完成机会。

@F101123
Universities often need many copies of the same material. Sharing a file can reduce the need to print and carry large piles of paper. | 大学常需要很多份相同资料，共享文件能减少印刷和搬运大量纸张的需要。
Students can also search for a word in a digital book. This can make finding a useful page quicker during study. | 学生还能在电子书里搜索单词，学习时更快找到有用的一页。
I keep the notes in one folder and open them when needed. I do not need to print a new copy each time. | 我把笔记放在同一文件夹，需要时打开，不必每次重新打印。
Phones and computers can stop working. A broken screen or empty battery can stop a student from reading a digital book. | 手机和电脑可能无法使用，屏幕坏了或没电都可能让学生看不了电子书。
Paper books can also be easier for some students to use for long periods. A library should offer more than one way to read. | 有些学生长时间读纸质书更方便，图书馆应提供不止一种阅读方式。
If the library still has a paper copy, I can continue studying. Without it, I may have to wait until I can charge my phone. | 如果图书馆有纸质本，我能继续学；没有的话，可能要等手机充电。

@F101122
An event that affects us directly can leave a strong memory. We understand the result because we have felt it ourselves. | 直接影响我们的事情容易留下深刻记忆，因为亲自感受过，所以更理解结果。
Advice in a book may seem unimportant until a similar problem happens. Experience can show why that advice matters in real life. | 书里的建议在遇到类似问题前可能显得不重要，经验能让人理解它的实际作用。
I had to wait for the next bus and arrived late. After that day, I checked the time before leaving home. | 我不得不等下一班车，最后迟到了，从那以后出门前会看好时间。
Real tasks do not always go exactly as a book describes. Trying them helps people learn how to deal with small changes. | 实际任务不总和书中描述完全一样，亲手尝试能让人学会处理小变化。
Books can still explain the basic steps. The best learning often comes when people use that information to do something themselves. | 书本仍能解释基本步骤，但人们亲自用这些知识做事时，往往学得更好。
I noticed when the food needed more time and checked it again. Those small decisions became easier the next time I cooked. | 我发现食物还需要时间，就再检查一次，下次做饭时这些小决定就容易了。

@F101028
Students can compare the story with their own lives. This can make people from another time seem easier to understand. | 学生能把故事和自己的生活比较，更容易理解另一个时代的人。
Teachers do not need to cover every old detail. A few clear examples can show how society has changed over time. | 老师不用讲所有古老细节，几个清楚例子就能显示社会怎样随时间变化。
The family followed rules that were different from mine. Talking about those differences made the history lesson more interesting to me. | 故事中的家庭遵循和我家不同的规则，讨论这些差别让我更感兴趣。
Students may spend so much time checking words that they lose the main story. This can make reading feel slow and tiring. | 学生可能花太多时间查词，反而跟不上主要故事，阅读就慢而累。
Help should be simple and close to the text. Short notes and a clear classroom discussion can remove much of the difficulty. | 帮助应简单、贴近文本，简短注释和清楚的课堂讨论能消除很多困难。
After the explanation, I could follow the story without stopping so often. The play became more enjoyable once the language was clearer. | 解释后，我不用经常停下就能跟上故事，语言清楚后，戏剧也更有趣。

@F101010
People cannot visit every place or see every problem themselves. News provides part of the information they use to form opinions. | 人们不能亲自去每个地方、看每个问题，新闻提供了形成观点的部分信息。
The stories that receive the most attention may seem the most important. This can affect what people discuss with friends and family. | 得到最多关注的新闻可能显得最重要，影响人们和亲友讨论什么。
The report showed rubbish beside places where children played. I began to see the issue as a daily problem, not a distant one. | 报道显示孩子玩耍的地方有垃圾，我开始把它当作身边问题，而不是遥远问题。
A useful example can make a new habit look easy. People may be more willing to try it when the steps are clear. | 有用的示范能让新习惯看起来简单，步骤清楚时，人们更愿意尝试。
The effect is not always immediate. Repeated messages can slowly make a different action feel normal in daily life. | 影响不总立刻出现，反复的信息能慢慢让另一种行为成为日常习惯。
I kept the bag near the door so I would remember it. Soon, I took it with me every time I went shopping. | 我把袋子放在门边提醒自己，很快每次购物都会带上它。

@F101137
Travel often involves small questions about food, tickets and directions. A little language knowledge can make these moments much easier. | 旅行常要询问食物、票和方向，懂一点外语就能让这些小事容易很多。
Starting at school gives every student a chance to learn. They do not need to wait until a problem happens abroad. | 在学校开始学，让每个学生都有机会，不必等在国外遇到问题才学。
I can understand the answer and ask another question if needed. This gives me more confidence when I am in a new place. | 我能听懂回答，必要时再问，在陌生地方也更有信心。
Even a simple job may involve people from other countries. Clear communication can prevent mistakes and help customers feel welcome. | 即使简单工作也可能接触外国人，清楚交流能避免错误，让顾客感到受欢迎。
Students may not know which job they will do later. Learning a language gives them another useful skill for the future. | 学生可能还不知道将来做什么，学外语能给他们增加一项有用技能。
The worker can explain the price and the time clearly. The visitor can then choose the right ticket without confusion. | 员工能清楚解释价格和时间，游客就能不迷糊地选对票。
"""


def _parse():
    result = {}
    for section in DATA.strip().split('\n\n'):
        lines = section.splitlines()
        qid = lines[0][1:]
        assert len(lines) == 7, (qid, len(lines))
        result[qid] = [dict(zip(('en', 'zh'), line.split(' | ', 1))) for line in lines[1:]]
    assert len(result) == 37
    return result


EXTRAS = _parse()


def word_count(text):
    return len(re.findall(r'\S+', text))


def build_expansion(outline):
    extras = EXTRAS[outline['qid']]
    best = None
    for flags in itertools.product((False, True), repeat=6):
        if not any(flags[:3]) or not any(flags[3:]):
            continue
        bodies = []
        for body_index, key in enumerate(('body1', 'body2')):
            original = outline[key]
            offset = body_index * 3
            sentences = [dict(original[0], added=False), dict(original[1], added=False)]
            for local in (0, 1):
                if flags[offset + local]:
                    sentences.append(dict(extras[offset + local], added=True))
            sentences.append(dict(original[2], added=False))
            if flags[offset + 2]:
                sentences.append(dict(extras[offset + 2], added=True))
            sentences.append(dict(original[3], added=False))
            bodies.append(sentences)
        paragraphs = [
            dict(outline['opening'], sentences=[dict(outline['opening'], added=False)]),
            {'en': ' '.join(x['en'] for x in bodies[0]), 'zh': ''.join(x['zh'] for x in bodies[0]), 'sentences': bodies[0]},
            {'en': ' '.join(x['en'] for x in bodies[1]), 'zh': ''.join(x['zh'] for x in bodies[1]), 'sentences': bodies[1]},
            dict(outline['closing'], sentences=[dict(outline['closing'], added=False)]),
        ]
        count = word_count(' '.join(p['en'] for p in paragraphs))
        if not 210 <= count <= 225:
            continue
        # Prefer ~218 words and balanced body paragraphs, with at least two added details per body when possible.
        short_body = sum(sum(flags[i:i + 3]) < 2 for i in (0, 3))
        balance = abs(word_count(paragraphs[1]['en']) - word_count(paragraphs[2]['en']))
        score = (short_body, abs(count - 218), balance, sum(flags))
        if best is None or score < best[0]:
            best = (score, {'word_count': count, 'paragraphs': paragraphs})
    if best is None:
        raise ValueError(f"No 210–225-word expansion found for {outline['qid']}")
    return best[1]


def render_expanded_markdown(outlines):
    lines = [
        '# WE 37题：简单拓展版（210–225词）', '',
        '沿用极简提纲的观点、两个要点和常见例子，只在主体段补充解释与细节。每篇四段，中英文对照。', '',
        '词数只计算四段英文正文，不包括题目、标题、中文、标签或说明。例子为写作示例。', '',
        '| 序号 | 题目 | 英文正文词数 |', '|---|---|---|',
    ]
    for o in outlines:
        lines.append(f"| {o['index']} | {o['title']} | {o['expanded']['word_count']} |")
    for o in outlines:
        lines += ['', '---', '', f"## {o['index']:02d}. {o['title']}", '',
                  o['title_en'], '', '**题号：** ' + ' / '.join('#' + q for q in o['qids']), '',
                  '**英文原题：** ' + o['question']['en'], '', o['question']['zh'], '',
                  f"**英文正文：{o['expanded']['word_count']}词**", '']
        if o.get('note'):
            lines += ['**问法提醒：** ' + o['note'], '']
        for number, p in enumerate(o['expanded']['paragraphs'], 1):
            lines += [f'### 第{number}段', '', p['en'], '', p['zh'], '']
    return '\n'.join(lines)
