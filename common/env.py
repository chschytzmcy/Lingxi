
import os
from langchain_community.chat_models.tongyi import ChatTongyi

os.environ["DEEPSEEK_API_KEY"] = "sk-850bedd4481947d581654de928ee0a5c"
os.environ["DASHSCOPE_API_KEY"] = "sk-791d6c7cc3094af99290577b709b47e6"
os.environ["TAVILY_API_KEY"] = "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"

# 设置 langsmith
# ###LANGCHAIN_TRACING_V2是设置LangChain是否开启日志跟踪模式。
os.environ['LANGSMITH_TRACING']="true"

###LANGCHAIN_API_KEY就是上面生成的LangSmith的key。
os.environ['LANGSMITH_API_KEY']="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"
os.environ['LANGSMITH_ENDPOINT']="https://api.smith.langchain.com"

###LANGCHAIN_PROJECT 是要跟踪的项目名称，如果LangSmith平台上还没有这个项目，会自动创建。如果不设置这个环境变量，会把相关信息写到default项目。这里的项目不一定要跟你实际的项目一一对应，可以理解为分类或者标签。你只要在运行某个应用前改变这一项，就会把相关的日志写到这个下面。
###可以按开发、生产环境分，也可以按日期分等等。
os.environ['LANGSMITH_PROJECT']="pr-dependable-yak-6"