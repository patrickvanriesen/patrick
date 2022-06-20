
function close_modal(modal_id)
{
var modal = document.getElementById(modal_id);
modal.style.display = "none";
}

function open_modal(modal_id)
{
var modal = document.getElementById(modal_id);
modal.style.display = "block";
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


function delete_role(role)
{
 var delete_role_form = document.getElementById('delete_role_form');
 var delete_role_input = document.getElementById('delete_role');
 delete_role_input.value = role;
 delete_role_form.submit();
}

function open_task_modal(modal_id, task_id)
{
open_modal(modal_id);

var task = document.getElementsByName(task_id);
// pass input from task value to modal
document.getElementById('task_modal_head_description').innerHTML = task[1].value;
document.getElementById('task_start_date').innerHTML = task[6].value;
document.getElementById('task_end_date').innerHTML = task[7].value;
document.getElementById('task_zone').innerHTML = task[5].value;
document.getElementById('task_building').innerHTML = task[4].value;
document.getElementById('task_duration').innerHTML = task[8].value + ' minutes';
document.getElementById('task_responsible').innerHTML = task[2].value;
document.getElementById('task_finishedBY').innerHTML = task[15].value;
document.getElementById('task_finishedON').innerHTML = task[14].value;
document.getElementById('task_verifiedBY').innerHTML = task[17].value;
document.getElementById('task_verifiedON').innerHTML = task[16].value;
document.getElementById('task_status').innerHTML = task[10].value;
// if re-occurs > 0 say yes else say no
if (task[11].value > 0)
{document.getElementById('task_reoccurs').innerHTML = 'Yes';
} else {document.getElementById('task_reoccurs').innerHTML = 'No';}

document.getElementById('task_instruction').innerHTML = task[12].innerHTML;
document.getElementById('task_issue').innerHTML = task[13].value;
document.getElementById('finish_task').value = task[0].value;
}

function finish_task()
{
var form = document.getElementById('finish_task_form');
form.submit();
}