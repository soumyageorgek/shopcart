var x_cord=[];
var y_cord=[];
var lines=[];
var line=[];
var radius=8;
var dn=0;
var da=0;
var flag=0
var example;
var context;

function init() 
{
	example = document.getElementById("a");
	context = example.getContext('2d');
	context.strokeStyle='black';
	context.font ="30pt Arial";
	context.lineWidth = 1;
}
function draw_node()
{
        if(da==1)
        {
                example.removeEventListener("click", draw_line, false);
                da=0;
        }
        example.addEventListener("click", draw, false);
        dn=1;
}
function draw_arc()
{
        if(dn==1)
        {
                example.removeEventListener("click", draw, false);
                dn=0;
        }
        example.addEventListener("click", draw_line, false);
        da=1;
}
function post()
{
        nest_list=make_list();
	new_list="[";
	for(i=0;i<nest_list.length;i++)
	{
		if(i==0)
		{
			new_list=new_list+"["+nest_list[i]+"]";
		}
		else
		{
			new_list=new_list+",["+nest_list[i]+"]";
		}
	}
	new_list=new_list+"]";
	alert(new_list);
	$.post("/color/", { name: new_list },function(data){alert(data);})
}
function make_list()
{
	var x;
	var i;
	var new_list=[];
	for(i=0;i<x_cord.length;i++)
	{
		new_list[i]=[];
	}
	for(i=0;i<lines.length;i++)
	{	
		new_list[(lines[i])].push((lines[i+1]));
		new_list[lines[i+1]].push(lines[i]);
		i++;
	}
	return new_list;
}

function draw(e)
{
	var x;
	var y;
	var i;

	x = e.pageX;
	y = e.pageY;
	i=bound_check(x,y);
	if(i==-1)
	{
		x_cord.push(x);
		y_cord.push(y);
		context.fillText(x_cord.length-1,x,y);
		context.fillStyle ="#B8D430";
		context.beginPath();
		context.arc(x, y, radius, 0, Math.PI * 2, false);
		context.closePath();
		context.stroke();
		context.fill();
	}
}
function draw_line(e)
{
	var x1=e.pageX;
	var y1=e.pageY;

	l=x_cord.length;
	i=bound_check(x1,y1);
	if(i==-1)
	{
		alert("Please select a node");
		return;
	}
	else
	{
		line.push(i);
		context.beginPath();
		context.arc(x_cord[i],y_cord[i], 1, 0, Math.PI * 2, false);
		context.closePath();
        	context.stroke();	
	}
	if(line.length==2)
	{
		if(line[0]==line[1])
		{
			line.pop();
		}
		else
		{
			i=line[0];
			j=line[1];
			lines.push(i);
			lines.push(j);
			context.beginPath();
			context.moveTo(x_cord[i],y_cord[i]);
			context.lineTo(x_cord[j],y_cord[j]);
			context.closePath();
			context.stroke();
			line=[];
		}
	}
}
function bound_check(x,y)
{
	for(i=0;i<x_cord.length;i++)
	{
                if(x<=(x_cord[i]+radius+3) && x>=(x_cord[i]-radius-3))
                {
                        if(y<=(y_cord[i]+radius+3) && y>=(y_cord[i]-radius-3))
                        {
                  	      return i;
                        }
                }
	}
	return -1;
}
