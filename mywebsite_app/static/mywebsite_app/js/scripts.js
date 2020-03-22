function openPopup(count){
    let popup_els = document.getElementsByClassName("popup-content");
    for(let i=0; i<popup_els.length; i++){
        popup_els[i].style.display = 'none';
    }
    popup_els[count].style.display = 'inline-block';

    $('.popupCloseButton').click(function(){
        $('.popup-content').hide();
    });
};