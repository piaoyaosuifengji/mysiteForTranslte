# mysiteForTranslte
mysiteForTranslte


需要完善：
    能不能考虑以特定的格式，语法，直接生成word文档？
        使用python-docx生成Word文档 ，可以最后直接导出来，你可以选择每次保存都导出来，或者只选择导出来一次
        可以在右边加入这样一个按钮就行了


    支持快捷键-0---------------------------------------------------------------重要
        1：保存
        2：调到下一个文本框里面
        3：能够临时保存一些 特定文本，在需要的时候快速复制，粘贴
    从文本在导入翻译---------------问题不大，因为反正你每次都是全部保存数据库中的数据-----不重要

    写一个计时器了解翻译的时间，只在页面是当前页面时有效-------------每个句子都单独计算时间，用来提醒自己---优先
                是不是可以用一个input或者按钮来显示时间信息


    每次都只能保存一个是一个问题：最好是在有修改而没有保存时给予提醒/或者是对有修改但未保存的有标记----不重要

    进行多线程的翻译，加快第一次加载速度--------不重要


    我的终极目标是英汉翻译达到2小时翻译1000英文单词（包括语法校正）
    加入一个一次性保存全部的按钮------以后稳定了就可以加入了，不然没什么用处


翻译流程安排：

1：文档准备
    -因为编辑会提供一个原始文件，你可以直接用就好了，也可以从网站上重新获取一个，以免有什么遗漏
    -创建一个txt格式的英文文件，用来提供翻译的数据

2：翻译环境初始化
    -打开网页就是了

3：翻译
    注意事项
        -题目可以留到最后翻译，如果不好翻译的话（小标题也是）
        -加快第一遍翻译的速度
        -如果第一遍翻译碰到感觉难翻译的句子直接跳过，做好标记----------加入这个标记需要再次翻译的功能

4：语句通顺性检查--------最后通读一遍，再翻译之前标记过的东西
5：语法检查
6：最后检查，提交