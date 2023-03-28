
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

function fill_in_info_task_modal(task_id)
{
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

function dynamic_styling(modal_id, task_id)
{
var modal = document.getElementById('task_modal_content');
var task = document.getElementsByName(task_id);

var task_status = task[10].value;
var center = document.getElementById('task_modal_full_center');
var task_error = document.getElementById('task_issue_part');
var task_error_line = document.getElementById('task_issue_line');
var task_error_header = document.getElementById('task_issue_header');
var task_row_verified = document.getElementById('task_row_verified');
var task_row_finished = document.getElementById('task_row_finished');

document.getElementById('task_issue').innerHTML = task_status;

// now use status as 'filter' but could also use user restriction as filter will think about it.
if (task[10].value === "new"){
modal.style = "height:60%;padding:50px;padding-top:20px;"
center.style = "display:flex; justify-content: space-between; height:60%; flex-direction: row;"
task_error.style = "display:none;"
task_error_line.style = "display:none;"
task_error_header.style = "display:none;"
task_row_verified.style = "display:none;"
task_row_finished.style = "display:none"

}else{
modal.style = "height:80%;padding:50px;padding-top:20px;"
center.style = "display:flex; justify-content: space-between; height:75%; flex-direction: row-reverse;"
task_error.style = "background-color:#009681; width:100%; height:150px; color:white;"
task_error_line.style = "width:100%; margin:5px; height:1px;"
task_error_header.style = "display:block;";
task_row_verified.style = "display:flex;";
task_row_finished.style = "display:flex";
}

}

function open_task_modal(modal_id, task_id)
{
open_modal(modal_id);
fill_in_info_task_modal(task_id);
dynamic_styling(modal_id, task_id);
}


function finish_task()
{
var form = document.getElementById('finish_task_form');
form.submit();
}

function open_task_option_modal(modal_id, task_id)
{
open_modal(modal_id);
var task = document.getElementsByName(task_id);
document.getElementById('task_option_desc').innerHTML = task[1].value
document.getElementById('cancel_task').value = task_id
}

function cancel_task()
{
var form = document.getElementById('cancel_task_form');
form.submit();
}




