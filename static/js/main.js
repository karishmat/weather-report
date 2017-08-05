/**
 * Created by karishma on 05/08/17.
 */

/**-------------------------------error box close btn ----------------*/

$(".dropdown-menu li a").click(function(){
  $(".btn:first-child").html($(this).text()+' <span class="caret"></span>');
});
