
//make sure add course row has same height as slap row
var forPreProc_addCourse = document.getElementById("addCourseRow");
var forPreProc_courseSlap = document.getElementById("courseSlap");
var forPreProc_spaceSlapList = document.body.querySelectorAll("div[id='spaceSlap']");
if(forPreProc_courseSlap.offsetHeight > forPreProc_addCourse.offsetHeight){
  forPreProc_addCourse.style.height = `${forPreProc_courseSlap.offsetHeight}px`;
  for(i=0; i < forPreProc_spaceSlapList.length; i++){
    forPreProc_spaceSlapList[i].style.height = `${forPreProc_courseSlap.offsetHeight}px`;
  }
}else {
  forPreProc_courseSlap.style.height = `${forPreProc_addCourse.offsetHeight}px`;
  for(i=0; i < forPreProc_spaceSlapList.length; i++){
    forPreProc_spaceSlapList[i].style.height = `${forPreProc_addCourse.offsetHeight}px`;
  }
}
