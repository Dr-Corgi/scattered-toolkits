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
