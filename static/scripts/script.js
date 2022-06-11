
function open_task_modal()
{
var modal = document.getElementById('task_modal');
modal.style.display = "block";
}

function open_task_modal_full()
{
var modal = document.getElementById('task_modal_full');
modal.style.display = "block";
}

function close_task_modal()
{
var modal = document.getElementById('task_modal');
modal.style.display = "none";
}

function close_task_modal_full()
{
var modal = document.getElementById('task_modal_full');
modal.style.display = "none";
}

function open_add_task_modal()
{
var modal = document.getElementById('add_task_modal');
modal.style.display = "block";
}


function close_add_task_modal()
{
var modal = document.getElementById('add_task_modal');
modal.style.display = "none";
}


function add_zone_color_change()
{
var select = document.getElementById('zone_color_select');
select.style.backgroundColor = select.value;
}