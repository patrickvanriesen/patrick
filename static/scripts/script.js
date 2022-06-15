
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

function delete_building(building)
{
var building_form = document.getElementById('building_form');
var building_input = document.getElementById('delete_building');
building_input.value = building;
building_form.submit();
}


function delete_role
{
 var delete_role_form = document.getElementById('delete_role_form');
 var delete_role_input = document.getElementById('delete_role');
 delete_role_input.value = delete_role;
 delete_role_form.submit();
}