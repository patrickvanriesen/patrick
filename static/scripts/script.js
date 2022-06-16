
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

