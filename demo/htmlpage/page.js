var PAGE_SIZE = 3;
function page_show(items, page, page_count, page_current_num, page_info, next_btn, prev_btn){
  console.log("page_show");
  if (page == 0 || page > (Math.ceil(items.length / page_count))){
    return;
  };
  var start = (page - 1) * page_count;
  if (start > items.length){
    return;
  };
  var end = Math.min(items.length, start + page_count);
  console.log("start:%d,end:%d", start, end);
  page_current_num.text(page);
  items.hide();
  for(var i = start; i < end; i++){
    items.eq(i).show();
  }
  if (page_info != null){
    page_info.text("page " + String(page) + " of " + String(
      Math.ceil(items.length / page_count)));
  }
};

function page_go(o, num, is_absolute){
  // is_absolute == true, num -1 is end
  var $page=$(o).closest(".page");
  var next = 0;
  var $page_content = $page.prev().find(".page-content");
  var $current_page_num = $page.find(".current-page");
  if (is_absolute){
    if (num > 0){
      next = num;
    }
    else{
      next = Math.ceil($page_content.children(":gt(0)").length / PAGE_SIZE);
    }
  }
  else{
    next = Number($current_page_num.text()) + num;
  }
  $page.find(".page-item-count").text("共" +String($page_content.children(":gt(0)").length) + "记录");
  console.log($page);
  console.log("current-page-num:%d", $current_page_num.text());
  console.log($page_content);
  page_show($page_content.children(":gt(0)"), next, PAGE_SIZE, $page.find(".current-page"), $page.find(".page-info"),
            $page.find(".next-page"), $page.find(".prev-page")
           );
}

$(document).ready(function(){
    console.log($(".next-page").length);
    for(var i=0; i < $(".next-page").length;i++){
      console.log($(".next-page").eq(i));
      page_go($(".next-page").eq(i), 1, true);
    };
    $(".next-page").click(function () {
      page_go(this, 1, false);
    });
    $(".prev-page").click(function () {
      page_go(this, -1, false);
    });
    $(".start-page").click(function(){
      page_go(this, 1, true);
    });
    $(".end-page").click(function(){
      page_go(this, -1, true);
    });
});
