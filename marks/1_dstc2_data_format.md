## Log Object
#### 1) session-id
当前调用(Call)的唯一ID
#### 2) session-date
调用的日期，为yyyy-mm-dd格式（string)
#### 3) session-time
调用的时间，为hh:mm:ss格式
#### 4) caller-id
调用者(Caller)的唯一ID
#### 5) system-specific
与进行这次调用有关的系统（如对话管理器）的相关信息
#### 6) turns
一个log-turn对象列表，给出了系统的输出和捕捉到的用户响应
1. turn-index: 轮次(turn)的索引，从0开始
2. output:
  - transcript: 系统提示的文本（string）
  - dialog-acts: 系统提示对应的对话行为
  - start-time: 系统提示合成开始进行的时间（以秒为单位，float）
  - end-time: 系统提示合成结束的时间（以秒为单位，float）
  - aborted: 该提示是否已终止，因为系统认为存在来自用户的插入（boolean）
3. input:
  - start-time: 进入用户响应的时间（以秒为单位，float）
  - end-time: 用户响应结束的时间（以秒为单位，float）
  - audio-file: 磁盘上的记录的文件名
  - live: 对话管理器在调用时刻实际接收到的输入
  - [live] asr-hyps: 
  - [live/asr-hyps] asr-hyp: 由语音识别器假设的转录结果（string）
  - [live/asr-hyps] score: 识别器给出的假设分数。（float）
  - [live] slu-hyps:
  - [live/slu-hyps] slu-hyp: 解码用户所说的内容得到的对话行为假设。
  - [live/slu-hyps] score: 假设的概率，和应为1（float）
  - batch: 用户轮的ASR离线计算结果。仅在train和dev时可用。
  - [batch] asr-hyps: 同上
  - [batch] cnet:由ASR给出的混淆网络，
  - [batch/cnet] start: 该用户轮的开始时间
  - [batch/cnet] end: 该用户轮的结束时间
  - [batch/cnet] arcs: 该用户轮中的可能词语列表
  - [batch/cnet/arcs] word: 对应的词语，可能对应于“!null”
  - [batch/cnet/arcs] score: 对应的分数
