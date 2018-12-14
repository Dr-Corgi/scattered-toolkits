## I. User Actions

| act filed | slot field | description |
|-----------|------------|-------------|
| ack |-|确认。如"okay"|
| affirm |-|肯定。如"yes"|
| bye|-|尝试结束会话|
| hello|-|问好|
| help|-|向系统获得通用帮助|
| negate|-|否定|
| null |-|系统无法理解的内容|
| repeat|-|要求系统重复|
| reqalts|-|请求可选的建议|
| reqmore|-|请求更多信息|
| restart|-|请求系统从新开始|
| silence |-|用户没有说话|
| thankyou |-|表达感谢|
| confirm |(s, v)|确认。必须是有意义的槽s和本体中指定的可能值v。如“Is it in the west?”|
| deny |(s,v)|拒绝。必须是有意义的槽s和本体中指定的可能值v。如"I dont want something in the west."|
| inform |(s,v)|告知。必须是有意义的槽s和本体中指定的可能值v。如"It must be in the west."|
| request |("slot",s)|请求。必须是有意义的槽s。如"what part of town is it?"|

## II. System Actions
| act filed | slot field | description |
|-----------|------------|-------------|
|affirm|-|肯定|
|bye|-|再见|
|canthear|-|如果监测到长时间的沉默，提示使用系统|
|confirm-domain|-|确认用户在进行领域内的任务|
|negate|-|否定|
|repeat|-|要求用户重复|
|reqmore|-|询问用户是否需要更多信息|
|welcomemsg|-|问候|
|canthelp|-|告知用户槽列表的组合约束不满足数据库中的任何实体|
|canhelp.missing\_slot\_value|("slot",s)和("venue", v)|告知值v的槽s是未知的|
|expl-conf|(s,v)|明确确认用户对槽s的目标是v|
|impl-conf|(s,v)|隐含确认用户对槽s的目标是v|
|inform|(s,v)|通知槽s的值被接收为v|
|offer|("name", v)|向用户提议名为v的值|
|request|("slot",s)|询问用户对槽s的期望值|
|select|(s,v)|始终出现至少一个具有相同s但具有不同v的其他select行为。要求用户从建议值中选择他们对槽s的目标|
