<%inherit file="/base.mako"/>

<%def name="dropdown()">
<div id="menu">
<ul id="sddm">
    <li><a href="${c.location}index">Home</a></li>
    <li><a href="${c.location}About-Us">About Us</a></li>
	<li><a href="${c.location}News">News</a></li>
    <li><a onmouseover="mopen('m1')" onmouseout="mclosetime()">Brazilian Agriculture</a>
        <div id="m1" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
        	<a href="${c.location}Brazil-Crop-Acreage">Brazil Crop Acereage</a>
        	<a href="${c.location}Brazil-Crop-Cycles">Brazil Month-By-Month Crop Cycle</a>
        	<a href="${c.location}Brazil-Land-Utilization">Brazil Land Utilization</a>
        	<a href="${c.location}Brazilian-Infrastructure">Brazilian Infrastructure</a>
        	<a href="${c.location}Mato-Grosso-Railroad">Mato Grosso Railroad</a>
        </div>
    </li>
    <li><a onmouseover="mopen('m2')" onmouseout="mclosetime()">South American Agriculture</a>
        <div id="m2" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
        	<a href="${c.location}Argentina-Crop-Acreage">Argentina Crop Acreage</a>
        	<a href="${c.location}Argentina-Crop-Cycles">Argentina Month-By-Month Crop Cycle</a>
        	<a href="${c.location}Paraguay-Bolivia-Crop-Acreage">Paraguay and Bolivia Crop Acreage</a>
        </div>
    </li>
	<li><a onmouseover="mopen('m3')" onmouseout="mclosetime()">PhotoGallery</a>
        <div id="m3" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
        	<a href="${c.location}Photo-Gallery-1/1">Classic Brazilian Photos</a>
        	<a href="${c.location}Photo-Gallery-2/1">Photos of Brazilian Ag 2010</a>
        	<a href="${c.location}Photo-Gallery-3/1">Photos of Brazilian Ag 2011</a>
        </div>
    </li>
    
    
    <li><a onmouseover="mopen('m4')" onmouseout="mclosetime()">Brazilian Biofuels</a>
        <div id="m4" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
        	<a href="${c.location}Brazil-Sugarcane-Ethanol-Industries">Brazil Sugarcane and Ethanol Industries</a>
        	<a href="${c.location}Brazil-US-Ethanol-Production">Brazil vs. U.S. Ethanol</a>
        	<a href="${c.location}How-Brazil-Created-The-International-Ethanol-Boom">How Brazil Created The International Ethanol Boom</a>
        	<a href="${c.location}Tri-Flex-Car">Tri-Flex Car</a>
        </div>
    </li>
    <li><a href="${c.location}Frequently-Asked-Questions">FAQ</a></li>
	<li><a href="${c.location}Contact-Us">Contact Us</a></li>
</ul>
</div>
<div style="clear:both"></div>
</%def>

<%def name="body()">
${h.literal(c.content)}
</%def>

<%def name="pics()">
</%def>


<%def name="javapics()">
	<script type="text/javascript">
		var str = "";
		var used = new Array()
		function getRand(){
			var n = Math.floor(Math.random() * 249) + 1;
			var i;
			for (i = 0; i < used.length; i ++){
				while (n == used[i]){
					n = Math.floor(Math.random() * 249) + 1;
				}
			}
			var str = "";
			if (n < 10)
				{str = "00"};
			if (n < 100 && n > 9)
				{str = "0";}
			str = str+n;
			return str;
		}
		function showpic(){
			str = getRand();
			used[0] = str;
			var l1 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";
			str = getRand();
			used[1] = str;
			var l2 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";
			str = getRand();
			used[2] = str;
			var l3 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";
			str = getRand();
			used[3] = str;
			var l4 = "<a href=/photo3/"+str+".JPG><img width=200 src=/photo3/"+str+"sm.jpg></a><br/><br/>";
			document.getElementById('pics').innerHTML=l1+l2+l3+l4;
			t=setTimeout('showpic()',15000);
		}
	</script>

</%def>