# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 18/7/8 下午4:21
# # @Author  : Lihailin<415787837@qq.com>
# # @Desc    : 爬取太原市杏花岭区网站文件
# # @File    : crawTaiyuan.py
# # @Software: PyCharm
#
# from lxml import etree
# import crawBase
# import os
# import time
#
# class CrawTaiyuanXhl(crawBase.CrawBase):
#
#     def __init__(self):
#         super(CrawTaiyuanXhl, self).__init__()
#         self.startPhantomJS()
#
#     def pageSource(self):
#         '''
#         网页源码
#         :param ith: 总共的页数
#         :return:
#         '''
#         s1 = '''
#         <html><head>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
# <title>中国太原杏花岭</title>
# <link rel="stylesheet" type="text/css" href="/xinghl/base/js/pagination/public_onlyPage.css">
# <script type="text/javascript" src="/xinghl/base/js/jquery-1.6.2.js"></script>
# <script type="text/javascript" src="/xinghl/base/js/pagination/tpc.pagination.core.js"></script>
# <script type="text/javascript" src="/xinghl/base/js/pagination/tpc.pagination.ui.js"></script>
# <link href="/xinghl/web/template/xinghl/css/style.css" rel="stylesheet" type="text/css">
# <link href="/xinghl/web/template/xinghl/css/blue.css" rel="alternate stylesheet" type="text/css">
# <script>
# function changeClass(classId,className,classType)
# {
# 	$("#content_title").html(className);
# 	if(classType == 2){
# 		$("#classIntro").load("/xinghl/html/ajax_intro/index.jhtml?classid=" + classId);
# 	}else{
# 		$("#pageShow").pagination({
# 			UIType : 1, //1.底层样式 2.jquery.pagination.js样式 默认：1
# 			dataUrl : "list_date_article.jhtml?classid="+classId, //读取数据地址
# 		    countUrl : "list_article_count.jhtml?classid="+classId,
# 			item_per_page : 20,
# 			dataGrid : "dataGrid", //显示结果的容器ID
# 			completeFunc : function(index){
# 			}
# 		});
# 	}
# }
#
# function getUrlParam(name) {
#     var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
#     var r = window.location.search.substr(1).match(reg);  //匹配目标参数
#     if (r != null) return unescape(r[2]); return null; //返回参数值
# }
# </script>
# <style>
# .noBG{
# 	background: none;
# };
# </style>
# <link type="text/css" rel="stylesheet" href="chrome-extension://pioclpoplcdbaefihamjohnefbikjilc/content.css"></head>
# <body>
# <!-- 顶部链接 -->
# <!-- 页眉 -->
#
# <div class="mainwrap">
# 	<!-- 图片版本 -->
# 	<img src="/xinghl/web/template/xinghl/img/xhlheader.jpg" width="950" height="170">
# 	<div class="maincontent">
#
# 		<div class="headbar">
#
# 			<div class="headbar_l">
# 				<a href="/xinghl" target="_blank"><img src="/xinghl/web/template/xinghl/img/headbar_1.gif">杏花岭区委</a>
#
# 				<a target="_blank" href="#"><img src="/xinghl/web/template/xinghl/img/headbar_2.gif">杏花岭区人大</a>
#
# 				<a href="/xinghl"><img src="/xinghl/web/template/xinghl/img/headbar_2.gif">杏花岭区政府</a>
#
# 				<a target="_blank" href="/xinghl/html/zhengx/index.jhtml"><img src="/xinghl/web/template/xinghl/img/headbar_3.gif">杏花岭区政协</a>
# 			</div>
# 		</div>
#
# 		<div id="header"></div>
#
# 		<!-- 导航 -->
#
# 		<div id="nav">
# 			<ul>
# 				  <li><a href="/xinghl/index.jhtml">首页</a></li>
# 								<li>
# 											<a target="" href="/xinghl/child/qqgk/index.jhtml" title="区情概况">区情概况</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/xhyw/index.jhtml" title="杏花要闻">杏花要闻</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/zwgk/index.jhtml" title="政务公开">政务公开</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/ztzl/index.jhtml" title="专题专栏">专题专栏</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/swxh/index.jhtml" title="商务杏花">商务杏花</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/mszx/index.jhtml" title="民生在线">民生在线</a>
# 								</li>
# 								<li>
# 									<a target="" href="http://www.sxtyxhl.gov.cn/xhl/zixun.jsp" title="领导信箱">领导信箱</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/article/tzgg05/index.jhtml" title="通知公告">通知公告</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/csmp/index.jhtml" title="城市名片">城市名片</a>
# 								</li>
# 			</ul>
# 		</div>
#
# 		<!-- 通知、搜索 -->
#
# 		<div class="navbar">
#
# 			<!-- <div class="notice">
# 				<form action="" method="post"
# 					name="searchform" target="_blank">
#
# 					<img src="/xinghl/web/template/xinghl/img/search_icon.gif" width="16" height="16" align="absmiddle" /> 全文检索
#
#           <input type="text" size="40"  name="searchword" value="请输入关键字" onfocus="searchFocus(this)" onblur="searchBlur(this)"/>
#
#           <input type="button" name="imageField" id="imageField" class="search_btn" value="搜 索" onclick="searchkey()"/>
#
#         </form>
# 			</div>
# 			 -->
#
# 			<div class="search" style="float: right;">
#
# 				<div class="date">
# 					<script language="JavaScript">
#            today=new Date();
#            function initArray(){
#            this.length=initArray.arguments.length
#            for(var i=0;i<this.length;i++)
#            this[i+1]=initArray.arguments[i] }
#            document.write(today.getFullYear(),"年",today.getMonth()+1,"月",today.getDate(),"日");
#            var d=new initArray("星期日","星期一","星期二","星期三","星期四","星期五","星期六");
#         </script>2018年7月7日
#         <script language="javascript">document.write(d[today.getDay()+1]);
#         </script>星期六
# 				</div>
#
# 				<div class="headbar_r" id="weather">
#
# 					<script>
#
# //loadData("weather","weather.jsp");
#
# </script>
#
# 				</div>
#
# 			</div>
#
# 		</div>
#     <!-- 内容 -->
#
#     <div class="wrap">
#
#       <!-- 左侧菜单 -->
#
#       <div class="left">
#
#
#         <div class="menu">
#           <div class="menu_title">		政务公开
# </div>
#           <ul>
# 					<li><a href="javascript:changeClass('3fa1f2b954ca41e38a7aecd726bfa90e','政策法规',1);">政策法规 </a></li>
# 					<li><a href="javascript:changeClass('ed4861f0cc9a4a7fa507d46dc88f59e2','应急管理',1);">应急管理 </a></li>
# 					<li><a href="javascript:changeClass('cacb176898e54e8da41dbf833e1bb4fa','人事任免',1);">人事任免 </a></li>
# 					<li><a href="javascript:changeClass('c93194fe269d44178800cfebc88feb21','工作报告',1);">工作报告 </a></li>
# 					<li><a href="javascript:changeClass('2101cc110adf465b9851298e03b6af75','统计数据',1);">统计数据 </a></li>
#           </ul>
#           <div class="menu_btm"></div>
#         </div>
#         <div class="hot">
#
#           <div class="title_s">点击热门</div>
#
#           <div class="box_content">
#
#             <ul>
#             </ul>
#
#           </div>
#
#         </div>
#
#       </div>
#
#       <!-- 右侧内容 -->
#
#       <div class="center_right" id="youb">
# <!-- 右侧内容 -->
#
#    <div class="content_title" id="content_title">政策法规</div>
# 		<!-- 文章列表 -->
#         <div class="list">
#           <ul id="dataGrid">    <!-- 文章列表 -->
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a808095645f0e9a01646307dc990a15.jhtml" title="全国人民代表大会常务委员会关于全国人民代表大会宪法和法律委员会职责问题的决定" class="arrow_1">
# 						全国人民代表大会常务委员会关于全国人民代表大会宪法和法律委员会职责问题的决定
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						07-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a80809563c3a0b20163c87ccdda07a6.jhtml" title="不动产登记资料查询暂行办法" class="arrow_1">
# 						不动产登记资料查询暂行办法
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						06-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a80809562ece1390163211673ff29da.jhtml" title="国务院办公厅关于印发2018年政务公开工作要点的通知" class="arrow_1">
# 						国务院办公厅关于印发2018年政务公开工作要点的通知
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						05-02
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a808095628e206a0162a337a87d13f5.jhtml" title="国务院办公厅关于印发科学数据管理办法的通知" class="arrow_1">
# 						国务院办公厅关于印发科学数据管理办法的通知
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						04-08
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a80809561f4ee020161f53208160071.jhtml" title="中华人民共和国反不正当竞争法" class="arrow_1">
# 						中华人民共和国反不正当竞争法
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						03-05
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a808095611bb8870161760636e04756.jhtml" title="国务院关于修改《行政法规制定程序条例》的决定" class="arrow_1">
# 						国务院关于修改《行政法规制定程序条例》的决定
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						02-08
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a80809560d51cee0160d98a92e00458.jhtml" title="中共中央办公厅 国务院办公厅印发《关于推进城市安全发展的意见》" class="arrow_1">
# 						中共中央办公厅 国务院办公厅印发《关于推进城市安全发展的意见》
# 						</a>
# 						<span class="date" style="">
# <!--						2018-->
# 						01-09
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a808095605431bb01606c680f7b092a.jhtml" title="太原市城市地下管网条例" class="arrow_1">
# 						太原市城市地下管网条例
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						12-19
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a8080955f9a647c015f9af231f001ba.jhtml" title="中华人民共和国统计法实施条例" class="arrow_1">
# 						中华人民共和国统计法实施条例
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						11-08
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8a8080955f08c61e015f090fa3440072.jhtml" title="中华人民共和国安全生产法" class="arrow_1">
# 						中华人民共和国安全生产法
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						10-11
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/43ebdbaa6fe6495aa6b9d0835b2d3966.jhtml" title="中华人民共和国中医药法" class="arrow_1">
# 						中华人民共和国中医药法
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						09-06
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/78c5afdaad2141b0aba061a51ecf1937.jhtml" title="中华人民共和国国家情报法" class="arrow_1">
# 						中华人民共和国国家情报法
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						08-06
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/a5a258b1885f407180c5f99ae43a1f33.jhtml" title="中华人民共和国公共文化服务保障法" class="arrow_1">
# 						中华人民共和国公共文化服务保障法
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						07-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/e9ab1faae3f04195906575982f9daa99.jhtml" title="中华人民共和国野生动物保护法" class="arrow_1">
# 						中华人民共和国野生动物保护法
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						07-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/90ec29c07c3e406e83edaf0f721e540b.jhtml" title="太原市餐厨废弃物管理条例" class="arrow_1">
# 						太原市餐厨废弃物管理条例
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						06-19
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8845a81e3af64132b42fb7c07982a8e5.jhtml" title="太原市物业管理条例" class="arrow_1">
# 						太原市物业管理条例
# 						</a>
# 						<span class="date" style="">
# <!--						2017-->
# 						06-19
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/7154d258e6844f8eb0af099631534f80.jhtml" title="中华人民共和国公路法" class="arrow_1">
# 						中华人民共和国公路法
# 						</a>
# 						<span class="date" style="">
# <!--						2015-->
# 						06-19
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/f99caf9ddfb4418a8e683af1f24c47fc.jhtml" title="固定资产投资项目节能评估和审查暂行办法" class="arrow_1">
# 						固定资产投资项目节能评估和审查暂行办法
# 						</a>
# 						<span class="date" style="">
# <!--						2015-->
# 						06-17
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/9841ebaaf24a4fe2b8b9de4eeec9f049.jhtml" title="山西省发展和改革委员会关于抓紧开展固定资产投资项目节能评估和审查工作的通知&nbsp;" class="arrow_1">
# 						山西省发展和改革委员会关于抓紧开展固定资产投资项目节能评估和审查工作的通知&nbsp;
# 						</a>
# 						<span class="date" style="">
# <!--						2015-->
# 						06-17
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/b6ed491a8f4f4581bbb7b01946eaaa31.jhtml" title="山西省价格监测办法" class="arrow_1">
# 						山西省价格监测办法
# 						</a>
# 						<span class="date" style="">
# <!--						2015-->
# 						06-16
#
# 						</span>
# 					</li>
# </ul>
#            	 <script>
# 			$(function(){
# 				$("#pageShow").pagination({
# 					UIType : 1, //1.底层样式 2.jquery.pagination.js样式 默认：1
# 					dataUrl : "list_date_article.jhtml?classid=3fa1f2b954ca41e38a7aecd726bfa90e", //读取数据地址
# 				    countUrl : "list_article_count.jhtml?classid=3fa1f2b954ca41e38a7aecd726bfa90e",
# 					item_per_page : 20,
# 					dataGrid : "dataGrid", //显示结果的容器ID
# 					completeFunc : function(index){
# 					}
# 				});
# 			});
# 			</script>
#
#
#         </div>
#         <!-- 分页 -->
#         <div class="page_box" id="pageShow"><table class="pageBase"><tbody><tr><td class="pageleft">每页<span class="pagenum pageCount">20</span>行 共<span class="pagenum totalCount">29</span>行 共<span class="pagenum totalPage">2</span>页</td><td class="pageright"><a href="javascript:void(0);" class="goFirst disable">首页</a><a href="javascript:void(0);" class="goPrev disable">上一页</a><a href="javascript:void(0);" class="goNext">下一页</a><a href="javascript:void(0);" class="goLast">末页</a> 当前页 <input name="textfield2" type="text" class="page-num" value=""><input type="button" name="Submit" value="GO" class="page-go"></td></tr></tbody></table></div>
# </div>
# </div>
# <div class="link">
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">中央部门网站</option>
#
#
#
# 	  	<option value="http://www.fmprc.gov.cn">中华人民共和国外交部</option>
#
#
#
# 	  	<option value="http://www.miit.gov.cn">中华人民共和国工业和信息化部</option>
#
#
#
# 	  	<option value="http://www.moe.edu.cn">中华人民共和国教育部</option>
#
#
#
# 	  	<option value="http://www.mps.gov.cn">中华人民共和国公安部</option>
#
#
#
# 	  	<option value="http://www.moc.gov.cn">中华人民共和国交通运输部</option>
#
#
#
# 	  	<option value="http://www.mlr.gov.cn">中华人民共和国国土资源部</option>
#
#
#
# 	  	<option value="http://www.cin.gov.cn">中华人民共和国建设部</option>
#
#
#
# 	  	<option value="http://www.china-mor.gov.cn">中华人民共和国铁道部</option>
#
#
#
# 	  	<option value="http://www.most.gov.cn">中华人民共和国科学技术部</option>
#
#
#
# 	  	<option value="http://www.moa.gov.cn">中华人民共和国农业部</option>
#
#
#
# 	  	<option value="http://www.mohrss.gov.cn">中华人民共和国人力资源和社会保障部</option>
#
#
#
# 	  	<option value="http://www.mwr.gov.cn">中华人民共和国水利部</option>
#
#
#
# 	  	<option value="http://www.mca.gov.cn">中华人民共和国民政部</option>
#
#
#
# 	  	<option value="http://www.mep.gov.cn">中华人民共和国环境保护部</option>
#
#
#
# 	  	<option value="http://www.moh.gov.cn">中华人民共和国卫生部</option>
#
#
#
# 	  	<option value="http://www.mohurd.gov.cn">中华人民共和国住房和城乡建设部</option>
#
#
#
# 	  	<option value="http://www.mofcom.gov.cn">中华人民共和国商务部</option>
#
#
#
# 	  	<option value="http://www.sdpc.gov.cn">中华人民共和国国家发展和改革委员会</option>
#
#
#
# 	  	<option value="http://www.mos.gov.cn">中华人民共和国监察部</option>
#
#
#
# 	  	<option value="http://www.moj.gov.cn">中华人民共和国司法部</option>
#
#
#
# 	  	<option value="http://www.mof.gov.cn">中华人民共和国财政部</option>
#
#
#
# 	  	<option value="http://www.chinapop.gov.cn">中华人民共和国国家人口和计划生育委员会</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">各省市政府网站</option>
#
#
#
# 	  	<option value="http://www.beijing.gov.cn">北京市</option>
#
#
#
# 	  	<option value="http://www.tj.gov.cn">天津市</option>
#
#
#
# 	  	<option value="http://www.shanghai.gov.cn">上海市</option>
#
#
#
# 	  	<option value="http://www.hebei.gov.cn">河北省</option>
#
#
#
# 	  	<option value="http://www.shanxigov.cn">山西省</option>
#
#
#
# 	  	<option value="http://www.ln.gov.cn">辽宁省</option>
#
#
#
# 	  	<option value="http://www.jl.gov.cn">吉林省</option>
#
#
#
# 	  	<option value="http://www.hlj.gov.cn">黑龙江省</option>
#
#
#
# 	  	<option value="http://www.nmg.gov.cn">内蒙古</option>
#
#
#
# 	  	<option value="http://www.jiangsu.gov.cn">江苏省</option>
#
#
#
# 	  	<option value="http://www.zj.gov.cn">浙江省</option>
#
#
#
# 	  	<option value="http://www.ah.gov.cn">安徽省</option>
#
#
#
# 	  	<option value="http://www.fujian.gov.cn">福建省</option>
#
#
#
# 	  	<option value="http://www.jiangxi.gov.cn">江西省</option>
#
#
#
# 	  	<option value="http://www.shandong.gov.cn/">山东省</option>
#
#
#
# 	  	<option value="http://www.henan.gov.cn">河南省</option>
#
#
#
# 	  	<option value="http://www.hubei.gov.cn/">湖北省</option>
#
#
#
# 	  	<option value="http://www.hunan.gov.cn/">湖南省</option>
#
#
#
# 	  	<option value="http://www.gd.gov.cn">广东省</option>
#
#
#
# 	  	<option value="http://www.gxi.gov.cn">广西省</option>
#
#
#
# 	  	<option value="http://www.hainan.gov.cn">海南省</option>
#
#
#
# 	  	<option value="http://www.cq.gov.cn">重庆市</option>
#
#
#
# 	  	<option value="http://www.sc.gov.cn">四川省</option>
#
#
#
# 	  	<option value="http://www.gzgov.gov.cn">贵州省</option>
#
#
#
# 	  	<option value="http://www.yn.gov.cn">云南省</option>
#
#
#
# 	  	<option value="http://www.xizang.gov.cn">西藏自治区</option>
#
#
#
# 	  	<option value="http://www.shaanxi.gov.cn">陕西省</option>
#
#
#
# 	  	<option value="http://www.gansu.gov.cn">甘肃省</option>
#
#
#
# 	  	<option value="http://www.qh.gov.cn">青海省</option>
#
#
#
# 	  	<option value="http://www.nx.gov.cn">宁夏自治区</option>
#
#
#
# 	  	<option value="http://www.xinjiang.gov.cn">新疆自治区</option>
#
#
#
# 	  	<option value="http://www.chinataiwan.org">中国台湾</option>
#
#
#
# 	  	<option value="http://www.gov.hk">中国香港</option>
#
#
#
# 	  	<option value="http://portal.gov.mo">中国澳门</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">政网导航</option>
#
#
#
# 	  	<option value="http://www.taiyuan.gov.cn/">太原市</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">新闻媒体网站</option>
#
#
#
# 	  	<option value="http://www.people.com.cn">人民日报</option>
#
#
#
# 	  	<option value="http://www.sxrb.com">山西日报</option>
#
#
#
# 	  	<option value="http://www.cntv.cn">中央电视台</option>
#
#
#
# 	  	<option value="http://www.gmw.cn">光明日报社</option>
#
#
#
# 	  	<option value="http://zqb.cyol.com">中国青年报</option>
#
#
#
# 	  	<option value="http://www.tynews.com.cn">太原新闻网</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">友情链接</option>
#
#
#
# 	  	<option value="http://www.tyxd.gov.cn">小店区</option>
#
#
#
# 	  	<option value="http://www.yingze.gov.cn">迎泽区</option>
#
#
#
# 	  	<option value="http://www.tyjcp.gov.cn">尖草坪区</option>
#
#
#
# 	  	<option value="http://www.sxtywbl.gov.cn&nbsp;">万柏林区</option>
#
#
#
# 	  	<option value="http://www.jinyuan.gov.cn">晋源区</option>
#
#
#
# 	  	<option value="http://www.sxgujiao.gov.cn">古交市</option>
#
#
#
# 	  	<option value="http://www.sxyangqu.gov.cn">阳曲县</option>
#
#
#
# 	  	<option value="http://www.qx.gov.cn">清徐县</option>
#
#
#
# 	  	<option value="http://www.sxlf.gov.cn">娄烦县</option>
#
#
#
#     </select>
#
#
#
#
#
# </div>
#
# <script>
#
# function newopen(newvalue)
#
# {
#
# 	if(newvalue!="")
#
# 	{
#
# 		window.open(newvalue);
#
# 	}
#
# }
#
# </script>
#
# <div id="footer">中共太原市杏花岭区委	&nbsp;&nbsp;&nbsp;太原市杏花岭区人民政府	&nbsp;&nbsp;&nbsp;主办&nbsp;&nbsp;&nbsp; © 2010 版权所有<br>
#
#      地址：山西省太原市杏花岭区胜利街99号　  邮箱：xinghualingqu@163.com　   <br>
#
# 	 技术支持： <a href="#" class="tpccn" target="_blank">山西优胜信息技术有限公司</a>&nbsp;&nbsp;&nbsp;&nbsp;
#
#
#
# 	 您是第<font style="font-weight:bolder;font-size:20px;font-style:italic">3179649</font> 位访客<br>
# 	<div style="width:300px;margin:0 auto; padding:20px 0;">
# 		 		<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=14010702070019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;">
# 				<img src="img/batb.png" style="float:left;">
# 				<p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">晋公网安备 14010702070019号</p>
# 			</a>
# 	</div>
# 	 <span>晋ICP备07002709号-1</span><span style="margin-left: 40px;">网站识别号:1401070001</span><br>
# <script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/06/113/0187/60682781/CA061130187606827810001.js' type='text/javascript'%3E%3C/script%3E"));</script><span id="_ideConac"><a href="//bszs.conac.cn/sitename?method=show&amp;id=314B966B930A03A0E053022819AC8BFE" target="_blank"><img id="imgConac" vspace="0" hspace="0" border="0" src="//dcs.conac.cn/image/red.png" data-bd-imgshare-binded="1"></a></span><script src="http://dcs.conac.cn/js/06/113/0187/60682781/CA061130187606827810001.js" type="text/javascript"></script><span id="_ideConac"></span>
#      <style type="text/css">
# 		#_span_jiucuo img{margin-bottom:15px}
# 	</style>
# 	 <script id="_jiucuo_" sitecode="1401070001" src="http://pucha.kaipuyun.cn/exposure/jiucuo.js"></script><span id="_span_jiucuo"><img onclick="Link('1401070001')" style="margin:0;border:0;cursor: pointer;" src="http://121.43.68.40/exposure/images/jiucuo.png?v=1401070001"></span>
#  </div>
#
# </div></div></body></html>
#         '''
#         s2 = '''
#         <html><head>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
# <title>中国太原杏花岭</title>
# <link rel="stylesheet" type="text/css" href="/xinghl/base/js/pagination/public_onlyPage.css">
# <script type="text/javascript" src="/xinghl/base/js/jquery-1.6.2.js"></script>
# <script type="text/javascript" src="/xinghl/base/js/pagination/tpc.pagination.core.js"></script>
# <script type="text/javascript" src="/xinghl/base/js/pagination/tpc.pagination.ui.js"></script>
# <link href="/xinghl/web/template/xinghl/css/style.css" rel="stylesheet" type="text/css">
# <link href="/xinghl/web/template/xinghl/css/blue.css" rel="alternate stylesheet" type="text/css">
# <script>
# function changeClass(classId,className,classType)
# {
# 	$("#content_title").html(className);
# 	if(classType == 2){
# 		$("#classIntro").load("/xinghl/html/ajax_intro/index.jhtml?classid=" + classId);
# 	}else{
# 		$("#pageShow").pagination({
# 			UIType : 1, //1.底层样式 2.jquery.pagination.js样式 默认：1
# 			dataUrl : "list_date_article.jhtml?classid="+classId, //读取数据地址
# 		    countUrl : "list_article_count.jhtml?classid="+classId,
# 			item_per_page : 20,
# 			dataGrid : "dataGrid", //显示结果的容器ID
# 			completeFunc : function(index){
# 			}
# 		});
# 	}
# }
#
# function getUrlParam(name) {
#     var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
#     var r = window.location.search.substr(1).match(reg);  //匹配目标参数
#     if (r != null) return unescape(r[2]); return null; //返回参数值
# }
# </script>
# <style>
# .noBG{
# 	background: none;
# };
# </style>
# <link type="text/css" rel="stylesheet" href="chrome-extension://pioclpoplcdbaefihamjohnefbikjilc/content.css"></head>
# <body>
# <!-- 顶部链接 -->
# <!-- 页眉 -->
#
# <div class="mainwrap">
# 	<!-- 图片版本 -->
# 	<img src="/xinghl/web/template/xinghl/img/xhlheader.jpg" width="950" height="170">
# 	<div class="maincontent">
#
# 		<div class="headbar">
#
# 			<div class="headbar_l">
# 				<a href="/xinghl" target="_blank"><img src="/xinghl/web/template/xinghl/img/headbar_1.gif">杏花岭区委</a>
#
# 				<a target="_blank" href="#"><img src="/xinghl/web/template/xinghl/img/headbar_2.gif">杏花岭区人大</a>
#
# 				<a href="/xinghl"><img src="/xinghl/web/template/xinghl/img/headbar_2.gif">杏花岭区政府</a>
#
# 				<a target="_blank" href="/xinghl/html/zhengx/index.jhtml"><img src="/xinghl/web/template/xinghl/img/headbar_3.gif">杏花岭区政协</a>
# 			</div>
# 		</div>
#
# 		<div id="header"></div>
#
# 		<!-- 导航 -->
#
# 		<div id="nav">
# 			<ul>
# 				  <li><a href="/xinghl/index.jhtml">首页</a></li>
# 								<li>
# 											<a target="" href="/xinghl/child/qqgk/index.jhtml" title="区情概况">区情概况</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/xhyw/index.jhtml" title="杏花要闻">杏花要闻</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/zwgk/index.jhtml" title="政务公开">政务公开</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/ztzl/index.jhtml" title="专题专栏">专题专栏</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/swxh/index.jhtml" title="商务杏花">商务杏花</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/mszx/index.jhtml" title="民生在线">民生在线</a>
# 								</li>
# 								<li>
# 									<a target="" href="http://www.sxtyxhl.gov.cn/xhl/zixun.jsp" title="领导信箱">领导信箱</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/article/tzgg05/index.jhtml" title="通知公告">通知公告</a>
# 								</li>
# 								<li>
# 											<a target="" href="/xinghl/child/csmp/index.jhtml" title="城市名片">城市名片</a>
# 								</li>
# 			</ul>
# 		</div>
#
# 		<!-- 通知、搜索 -->
#
# 		<div class="navbar">
#
# 			<!-- <div class="notice">
# 				<form action="" method="post"
# 					name="searchform" target="_blank">
#
# 					<img src="/xinghl/web/template/xinghl/img/search_icon.gif" width="16" height="16" align="absmiddle" /> 全文检索
#
#           <input type="text" size="40"  name="searchword" value="请输入关键字" onfocus="searchFocus(this)" onblur="searchBlur(this)"/>
#
#           <input type="button" name="imageField" id="imageField" class="search_btn" value="搜 索" onclick="searchkey()"/>
#
#         </form>
# 			</div>
# 			 -->
#
# 			<div class="search" style="float: right;">
#
# 				<div class="date">
# 					<script language="JavaScript">
#            today=new Date();
#            function initArray(){
#            this.length=initArray.arguments.length
#            for(var i=0;i<this.length;i++)
#            this[i+1]=initArray.arguments[i] }
#            document.write(today.getFullYear(),"年",today.getMonth()+1,"月",today.getDate(),"日");
#            var d=new initArray("星期日","星期一","星期二","星期三","星期四","星期五","星期六");
#         </script>2018年7月7日
#         <script language="javascript">document.write(d[today.getDay()+1]);
#         </script>星期六
# 				</div>
#
# 				<div class="headbar_r" id="weather">
#
# 					<script>
#
# //loadData("weather","weather.jsp");
#
# </script>
#
# 				</div>
#
# 			</div>
#
# 		</div>
#     <!-- 内容 -->
#
#     <div class="wrap">
#
#       <!-- 左侧菜单 -->
#
#       <div class="left">
#
#
#         <div class="menu">
#           <div class="menu_title">		政务公开
# </div>
#           <ul>
# 					<li><a href="javascript:changeClass('3fa1f2b954ca41e38a7aecd726bfa90e','政策法规',1);">政策法规 </a></li>
# 					<li><a href="javascript:changeClass('ed4861f0cc9a4a7fa507d46dc88f59e2','应急管理',1);">应急管理 </a></li>
# 					<li><a href="javascript:changeClass('cacb176898e54e8da41dbf833e1bb4fa','人事任免',1);">人事任免 </a></li>
# 					<li><a href="javascript:changeClass('c93194fe269d44178800cfebc88feb21','工作报告',1);">工作报告 </a></li>
# 					<li><a href="javascript:changeClass('2101cc110adf465b9851298e03b6af75','统计数据',1);">统计数据 </a></li>
#           </ul>
#           <div class="menu_btm"></div>
#         </div>
#         <div class="hot">
#
#           <div class="title_s">点击热门</div>
#
#           <div class="box_content">
#
#             <ul>
#             </ul>
#
#           </div>
#
#         </div>
#
#       </div>
#
#       <!-- 右侧内容 -->
#
#       <div class="center_right" id="youb">
# <!-- 右侧内容 -->
#
#    <div class="content_title" id="content_title">政策法规</div>
# 		<!-- 文章列表 -->
#         <div class="list">
#           <ul id="dataGrid">    <!-- 文章列表 -->
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/68de366066d64cd2a61d8cb860b8366e.jhtml" title="弘扬雷锋精神&nbsp;&nbsp;传承传统美德" class="arrow_1">
# 						弘扬雷锋精神&nbsp;&nbsp;传承传统美德
# 						</a>
# 						<span class="date" style="">
# <!--						2014-->
# 						03-11
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/7b3c26a34be74509a6b102f1b6ac9b06.jhtml" title="山西省发展和改革委员会关于抓紧开展固定资产投资项目节能评估和审查工作的通知" class="arrow_1">
# 						山西省发展和改革委员会关于抓紧开展固定资产投资项目节能评估和审查工作的通知
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						11-08
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/05489098ed014024860c0bf4ada9ff4e.jhtml" title="中华人民共和国公路法" class="arrow_1">
# 						中华人民共和国公路法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/2c2248f23f134e7d99f1c5adf74c2352.jhtml" title="全国人口普查条例" class="arrow_1">
# 						全国人口普查条例
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/db625ff134bf449f9f6d31560d5906e8.jhtml" title="国土资源标准化管理办法" class="arrow_1">
# 						国土资源标准化管理办法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						07-01
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/cb57ebb15f30440d83c4c9778b28ff8f.jhtml" title="太原市经济适用住房管理办法" class="arrow_1">
# 						太原市经济适用住房管理办法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/e9582a6c8f02452b96d94bd7a91df14b.jhtml" title="中华人民共和国矿产资源法" class="arrow_1">
# 						中华人民共和国矿产资源法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/6a92af3a8b3b47d6aa3ed3dfd532b9d5.jhtml" title="中华人民共和国专利法" class="arrow_1">
# 						中华人民共和国专利法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-04
#
# 						</span>
# 					</li>
# 					<li class="">
# 					<a target="_blank" href="/xinghl/article/zcfg/8d64213c20334afeb237d17491d450e8.jhtml" title="无照经营查处取缔办法" class="arrow_1">
# 						无照经营查处取缔办法
# 						</a>
# 						<span class="date" style="">
# <!--						2010-->
# 						08-03
#
# 						</span>
# 					</li>
# </ul>
#            	 <script>
# 			$(function(){
# 				$("#pageShow").pagination({
# 					UIType : 1, //1.底层样式 2.jquery.pagination.js样式 默认：1
# 					dataUrl : "list_date_article.jhtml?classid=3fa1f2b954ca41e38a7aecd726bfa90e", //读取数据地址
# 				    countUrl : "list_article_count.jhtml?classid=3fa1f2b954ca41e38a7aecd726bfa90e",
# 					item_per_page : 20,
# 					dataGrid : "dataGrid", //显示结果的容器ID
# 					completeFunc : function(index){
# 					}
# 				});
# 			});
# 			</script>
#
#
#         </div>
#         <!-- 分页 -->
#         <div class="page_box" id="pageShow"><table class="pageBase"><tbody><tr><td class="pageleft">每页<span class="pagenum pageCount">20</span>行 共<span class="pagenum totalCount">29</span>行 共<span class="pagenum totalPage">2</span>页</td><td class="pageright"><a href="javascript:void(0);" class="goFirst">首页</a><a href="javascript:void(0);" class="goPrev">上一页</a><a href="javascript:void(0);" class="goNext disable">下一页</a><a href="javascript:void(0);" class="goLast disable">末页</a> 当前页 <input name="textfield2" type="text" class="page-num" value=""><input type="button" name="Submit" value="GO" class="page-go"></td></tr></tbody></table></div>
# </div>
# </div>
# <div class="link">
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">中央部门网站</option>
#
#
#
# 	  	<option value="http://www.fmprc.gov.cn">中华人民共和国外交部</option>
#
#
#
# 	  	<option value="http://www.miit.gov.cn">中华人民共和国工业和信息化部</option>
#
#
#
# 	  	<option value="http://www.moe.edu.cn">中华人民共和国教育部</option>
#
#
#
# 	  	<option value="http://www.mps.gov.cn">中华人民共和国公安部</option>
#
#
#
# 	  	<option value="http://www.moc.gov.cn">中华人民共和国交通运输部</option>
#
#
#
# 	  	<option value="http://www.mlr.gov.cn">中华人民共和国国土资源部</option>
#
#
#
# 	  	<option value="http://www.cin.gov.cn">中华人民共和国建设部</option>
#
#
#
# 	  	<option value="http://www.china-mor.gov.cn">中华人民共和国铁道部</option>
#
#
#
# 	  	<option value="http://www.most.gov.cn">中华人民共和国科学技术部</option>
#
#
#
# 	  	<option value="http://www.moa.gov.cn">中华人民共和国农业部</option>
#
#
#
# 	  	<option value="http://www.mohrss.gov.cn">中华人民共和国人力资源和社会保障部</option>
#
#
#
# 	  	<option value="http://www.mwr.gov.cn">中华人民共和国水利部</option>
#
#
#
# 	  	<option value="http://www.mca.gov.cn">中华人民共和国民政部</option>
#
#
#
# 	  	<option value="http://www.mep.gov.cn">中华人民共和国环境保护部</option>
#
#
#
# 	  	<option value="http://www.moh.gov.cn">中华人民共和国卫生部</option>
#
#
#
# 	  	<option value="http://www.mohurd.gov.cn">中华人民共和国住房和城乡建设部</option>
#
#
#
# 	  	<option value="http://www.mofcom.gov.cn">中华人民共和国商务部</option>
#
#
#
# 	  	<option value="http://www.sdpc.gov.cn">中华人民共和国国家发展和改革委员会</option>
#
#
#
# 	  	<option value="http://www.mos.gov.cn">中华人民共和国监察部</option>
#
#
#
# 	  	<option value="http://www.moj.gov.cn">中华人民共和国司法部</option>
#
#
#
# 	  	<option value="http://www.mof.gov.cn">中华人民共和国财政部</option>
#
#
#
# 	  	<option value="http://www.chinapop.gov.cn">中华人民共和国国家人口和计划生育委员会</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">各省市政府网站</option>
#
#
#
# 	  	<option value="http://www.beijing.gov.cn">北京市</option>
#
#
#
# 	  	<option value="http://www.tj.gov.cn">天津市</option>
#
#
#
# 	  	<option value="http://www.shanghai.gov.cn">上海市</option>
#
#
#
# 	  	<option value="http://www.hebei.gov.cn">河北省</option>
#
#
#
# 	  	<option value="http://www.shanxigov.cn">山西省</option>
#
#
#
# 	  	<option value="http://www.ln.gov.cn">辽宁省</option>
#
#
#
# 	  	<option value="http://www.jl.gov.cn">吉林省</option>
#
#
#
# 	  	<option value="http://www.hlj.gov.cn">黑龙江省</option>
#
#
#
# 	  	<option value="http://www.nmg.gov.cn">内蒙古</option>
#
#
#
# 	  	<option value="http://www.jiangsu.gov.cn">江苏省</option>
#
#
#
# 	  	<option value="http://www.zj.gov.cn">浙江省</option>
#
#
#
# 	  	<option value="http://www.ah.gov.cn">安徽省</option>
#
#
#
# 	  	<option value="http://www.fujian.gov.cn">福建省</option>
#
#
#
# 	  	<option value="http://www.jiangxi.gov.cn">江西省</option>
#
#
#
# 	  	<option value="http://www.shandong.gov.cn/">山东省</option>
#
#
#
# 	  	<option value="http://www.henan.gov.cn">河南省</option>
#
#
#
# 	  	<option value="http://www.hubei.gov.cn/">湖北省</option>
#
#
#
# 	  	<option value="http://www.hunan.gov.cn/">湖南省</option>
#
#
#
# 	  	<option value="http://www.gd.gov.cn">广东省</option>
#
#
#
# 	  	<option value="http://www.gxi.gov.cn">广西省</option>
#
#
#
# 	  	<option value="http://www.hainan.gov.cn">海南省</option>
#
#
#
# 	  	<option value="http://www.cq.gov.cn">重庆市</option>
#
#
#
# 	  	<option value="http://www.sc.gov.cn">四川省</option>
#
#
#
# 	  	<option value="http://www.gzgov.gov.cn">贵州省</option>
#
#
#
# 	  	<option value="http://www.yn.gov.cn">云南省</option>
#
#
#
# 	  	<option value="http://www.xizang.gov.cn">西藏自治区</option>
#
#
#
# 	  	<option value="http://www.shaanxi.gov.cn">陕西省</option>
#
#
#
# 	  	<option value="http://www.gansu.gov.cn">甘肃省</option>
#
#
#
# 	  	<option value="http://www.qh.gov.cn">青海省</option>
#
#
#
# 	  	<option value="http://www.nx.gov.cn">宁夏自治区</option>
#
#
#
# 	  	<option value="http://www.xinjiang.gov.cn">新疆自治区</option>
#
#
#
# 	  	<option value="http://www.chinataiwan.org">中国台湾</option>
#
#
#
# 	  	<option value="http://www.gov.hk">中国香港</option>
#
#
#
# 	  	<option value="http://portal.gov.mo">中国澳门</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">政网导航</option>
#
#
#
# 	  	<option value="http://www.taiyuan.gov.cn/">太原市</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">新闻媒体网站</option>
#
#
#
# 	  	<option value="http://www.people.com.cn">人民日报</option>
#
#
#
# 	  	<option value="http://www.sxrb.com">山西日报</option>
#
#
#
# 	  	<option value="http://www.cntv.cn">中央电视台</option>
#
#
#
# 	  	<option value="http://www.gmw.cn">光明日报社</option>
#
#
#
# 	  	<option value="http://zqb.cyol.com">中国青年报</option>
#
#
#
# 	  	<option value="http://www.tynews.com.cn">太原新闻网</option>
#
#
#
#     </select>
#
#
#
#     <select name="select" id="select" onchange="newopen(this.value)">
#
#       <option value="">友情链接</option>
#
#
#
# 	  	<option value="http://www.tyxd.gov.cn">小店区</option>
#
#
#
# 	  	<option value="http://www.yingze.gov.cn">迎泽区</option>
#
#
#
# 	  	<option value="http://www.tyjcp.gov.cn">尖草坪区</option>
#
#
#
# 	  	<option value="http://www.sxtywbl.gov.cn&nbsp;">万柏林区</option>
#
#
#
# 	  	<option value="http://www.jinyuan.gov.cn">晋源区</option>
#
#
#
# 	  	<option value="http://www.sxgujiao.gov.cn">古交市</option>
#
#
#
# 	  	<option value="http://www.sxyangqu.gov.cn">阳曲县</option>
#
#
#
# 	  	<option value="http://www.qx.gov.cn">清徐县</option>
#
#
#
# 	  	<option value="http://www.sxlf.gov.cn">娄烦县</option>
#
#
#
#     </select>
#
#
#
#
#
# </div>
#
# <script>
#
# function newopen(newvalue)
#
# {
#
# 	if(newvalue!="")
#
# 	{
#
# 		window.open(newvalue);
#
# 	}
#
# }
#
# </script>
#
# <div id="footer">中共太原市杏花岭区委	&nbsp;&nbsp;&nbsp;太原市杏花岭区人民政府	&nbsp;&nbsp;&nbsp;主办&nbsp;&nbsp;&nbsp; © 2010 版权所有<br>
#
#      地址：山西省太原市杏花岭区胜利街99号　  邮箱：xinghualingqu@163.com　   <br>
#
# 	 技术支持： <a href="#" class="tpccn" target="_blank">山西优胜信息技术有限公司</a>&nbsp;&nbsp;&nbsp;&nbsp;
#
#
#
# 	 您是第<font style="font-weight:bolder;font-size:20px;font-style:italic">3179649</font> 位访客<br>
# 	<div style="width:300px;margin:0 auto; padding:20px 0;">
# 		 		<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=14010702070019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;">
# 				<img src="img/batb.png" style="float:left;">
# 				<p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">晋公网安备 14010702070019号</p>
# 			</a>
# 	</div>
# 	 <span>晋ICP备07002709号-1</span><span style="margin-left: 40px;">网站识别号:1401070001</span><br>
# <script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/06/113/0187/60682781/CA061130187606827810001.js' type='text/javascript'%3E%3C/script%3E"));</script><span id="_ideConac"><a href="//bszs.conac.cn/sitename?method=show&amp;id=314B966B930A03A0E053022819AC8BFE" target="_blank"><img id="imgConac" vspace="0" hspace="0" border="0" src="//dcs.conac.cn/image/red.png" data-bd-imgshare-binded="1"></a></span><script src="http://dcs.conac.cn/js/06/113/0187/60682781/CA061130187606827810001.js" type="text/javascript"></script><span id="_ideConac"></span>
#      <style type="text/css">
# 		#_span_jiucuo img{margin-bottom:15px}
# 	</style>
# 	 <script id="_jiucuo_" sitecode="1401070001" src="http://pucha.kaipuyun.cn/exposure/jiucuo.js"></script><span id="_span_jiucuo"><img onclick="Link('1401070001')" style="margin:0;border:0;cursor: pointer;" src="http://121.43.68.40/exposure/images/jiucuo.png?v=1401070001"></span>
#  </div>
#
# </div></div></body></html>
#         '''
#         return s1,s2
#
#     def firstPageT(self, c):
#         '''
#         http://www.sxtyxhl.gov.cn/xinghl/child/zwgk/index.jhtml, 获得该页面的'文件页面'链接
#         :param c: 网页源码
#         :return:
#         '''
#         sel = etree.HTML(c)
#         l = sel.xpath('//div[@class="list"]/ul/li/a/@href')
#         l = list(map(lambda x:'http://www.sxtyxhl.gov.cn/'+x, l))
#         # print(l)
#         return l
#
#     def firstPage(self):
#         '''
#         http://www.sxtyxhl.gov.cn/xinghl/child/zwgk/index.jhtml, 获得该页面的'文件页面'链接
#         包括点击下一页
#         '''
#         s1, s2 = self.pageSource()
#         r = []
#         r += self.firstPageT(s1)
#         r += self.firstPageT(s2)
#         print(r)
#         return r
#
#     def getUsefulInfo(self, url):
#         '''
#         访问url,并下载网页,并解析得到需要的信息
#         http://www.taiyuan.gov.cn/doc/2017/12/29/183470.shtml
#         :param url:
#         :return:
#         '''
#         c = self.getFromSelenium(url)
#         html = etree.HTML(c)
#         print(c)
#         xxmc = self.xpath_text(html, '//div[@class="article_title"]')  # 信息名称
#         print(xxmc)
#         # fbsj = url.split('/')[-2]
#         # # print(fbsj)
#         # nr = self.getContent(html, '//div[@class="news_content_center"]/p')
#         # # print(nr)
#         # tplj = {}
#         # return xxmc, fbsj, nr, tplj
#
#     def writeUsefulInfo(self, dic, url, xxmc, fbsj, nr, tplj):
#         '''
#         写数据到文本文件
#         :param wz: str, 位置(分类)
#         :param url: str, 网页链接
#         :param xxmc: str, 信息名称
#         :param fbrq: str, 发布日期
#         :param fbbm: str, 发布部门
#         :param nr: 内容
#         :return:
#         '''
#         xxmc = xxmc.replace('/','').replace(' ','')
#         fname = '%s/%s.txt' %(dic, xxmc)
#         with open(fname, 'w') as f:
#             f.write('网页地址: %s\n' %url)
#             f.write('索引号:    \n')
#             f.write('信息分类:    \n')
#             f.write('发布机构: 太原市教育局\n')
#             f.write('生成日期: %s\n' % fbsj)
#             f.write('生效日期:    \n')
#             f.write('废止日期:    \n')
#             f.write('信息名称: %s\n' % xxmc)
#             f.write('文   号:    \n')
#             f.write('关键词: \n')
#             f.write('内容:%s\n%s\n' % (nr, '\n'.join(tplj)))
#
#         picPath = '%s/%s' %(dic, xxmc)
#         print(picPath)
#         if len(tplj) > 0:
#             os.system('mkdir -p %s' %picPath)
#         for u in tplj:
#             n = u[-10:].replace('/','_').replace(' ','')
#             self._secureCrawFile(u, {}, '%s/%s'%(picPath, n))
#
#     def run(self, url, dic, ith):
#         '''
#         进入 first pase 开始爬取文章
#         :param url:
#         :param dic:
#         :param ith:总页数
#         :return:
#         '''
#         os.system('mkdir -p %s' % dic)  # 创建文件夹
#         for f in self.firstPage(url, ith):
#             xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj = self.getUsefulInfo(f)
#             self.writeUsefulInfo(dic, f, xxmc, syh, fbsj, fbly, wh, gjc, nr, tplj)
#
# if __name__ == '__main__':
#     pageInfo = 'http://www.sxtyxhl.gov.cn//xinghl/article/zcfg/8a808095645f0e9a01646307dc990a15.jhtml'
#     t = CrawTaiyuanXhl()
#     # t.firstPage()
#     t.getUsefulInfo(pageInfo)
#     # t.run(firstUri, '太原/市政府文件', 2)  # 市政府文件
