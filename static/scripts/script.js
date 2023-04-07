
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
// issue and instruction
document.getElementById('task_instruction').innerHTML = task[12].innerHTML;
document.getElementById('task_issue').innerHTML = task[13].value;
// task_id in the buttons
document.getElementById('finish_task').value = task[0].value;
// stores not/not easy reachable info for edit pallet
document.getElementById('role').value = task[3].value;
document.getElementById('duration').value = task[8].value;
document.getElementById('task_rowid').value = task[0].value;

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
// for some reason below does not work in fill in info part.. will figure out why ? :(
document.getElementById('task_rowid').value = task[0].value;
}
else{
modal.style = "height:80%;padding:50px;padding-top:20px;"
center.style = "display:flex; justify-content: space-between; height:75%; flex-direction: row-reverse;"
task_error.style = "background-color:#009681; width:100%; height:150px; color:white;"
task_error_line.style = "width:100%; margin:5px; height:1px;"
task_error_header.style = "display:block;";
task_row_verified.style = "display:flex;";
task_row_finished.style = "display:flex";
document.getElementById('task_modal_full_footer').style = "display:flex";
// for some reason below does not work in fill in info part.. will figure out why ? :(
if (task_status === "finished"){
document.getElementById('verify_task').value = task[0].value;
document.getElementById('reopen_task').value = task[0].value;}
// if completed, hide buttons. think about changing completed to verified
if (task_status === "Completed"){
document.getElementById('task_modal_full_footer').style = "display:none;"}

}
}


function open_task_modal(modal_id, task_id){
open_modal(modal_id);
dynamic_styling(modal_id, task_id);
fill_in_info_task_modal(task_id);
}

function open_task_modal_no_restyle(modal_id, task_id){
open_modal(modal_id);
fill_in_info_task_modal(task_id);
}



// replace all those function with a more generic post form function
function finish_task(){
var form = document.getElementById('finish_task_form');
form.submit();
}

function verify_task(){
var form = document.getElementById('verify_task_form');
form.submit();
}

function reopen_task(){
var form = document.getElementById('reopen_task_form');
form.submit();
}

function open_task_option_modal(modal_id, task_id){
open_modal(modal_id);
var task = document.getElementsByName(task_id);
document.getElementById('task_option_desc').innerHTML = task[1].value
document.getElementById('cancel_task').value = task_id
}

function cancel_task(task_id){
document.getElementById('cancel_task').value = task_id
var form = document.getElementById('cancel_task_form');
form.submit();
}


function edit_task_modal(modal_id)
{
// open modal
open_modal(modal_id)
var  task = document.getElementsByName(document.getElementById('task_rowid').value)
// retrieve info from SRC modal and fill in in the edit task modal
document.getElementById('edit_task_description').value = document.getElementById('task_modal_head_description').innerHTML ;
document.getElementById('edit_task_responsible').value = document.getElementById('task_responsible').innerHTML ;
// the selected part is is not working properly. and it used to do
document.getElementById('edit_task_role').value = task[3].value;
document.getElementById('edit_task_building').selected = document.getElementById('task_building').innerHTML;
document.getElementById('edit_task_zone').value = task[5].value ;
// this part is ok again
document.getElementById('edit_task_duration').value = task[8].value;
document.getElementById('edit_task_start_date').value = document.getElementById('task_start_date').innerHTML ;
document.getElementById('edit_task_due_date').value = document.getElementById('task_end_date').innerHTML ;
document.getElementById('edit_task_instruction').value = document.getElementById('task_instruction').innerHTML ;
document.getElementById('edit_task').value = task[0].value;
}

function open_issue_modal(){
open_modal('report_issue_modal')
var  task = document.getElementsByName(document.getElementById('task_rowid').value)
document.getElementById('Report_issue_id').value = task[0].value;
}

function link_to_home(){window.location.replace('/');}