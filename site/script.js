const photoDialog = document.querySelector('.photo-dialog');
const photoButtons = [...document.querySelectorAll('.photo-open')];
let photoIndex = 0;
function showPhoto(index) {
 photoIndex = (index + photoButtons.length) % photoButtons.length;
 const source = photoButtons[photoIndex].querySelector('img');
 const large = document.querySelector('#large-photo');
 large.src = source.src; large.alt = source.alt;
 document.querySelector('#large-caption').textContent = photoButtons[photoIndex].nextElementSibling.firstElementChild.textContent;
 document.querySelector('#photo-count').textContent = `${photoIndex + 1} / ${photoButtons.length}`;
}
photoButtons.forEach((button,index)=>button.addEventListener('click',()=>{showPhoto(index);photoDialog.showModal();}));
document.querySelector('.photo-close').addEventListener('click',()=>photoDialog.close());
document.querySelector('.photo-prev').addEventListener('click',()=>showPhoto(photoIndex-1));
document.querySelector('.photo-next').addEventListener('click',()=>showPhoto(photoIndex+1));
photoDialog.addEventListener('keydown',event=>{if(event.key==='ArrowRight'){event.preventDefault();showPhoto(photoIndex+1);}if(event.key==='ArrowLeft'){event.preventDefault();showPhoto(photoIndex-1);}});
photoDialog.addEventListener('click',event=>{if(event.target===photoDialog){const r=photoDialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)photoDialog.close();}});
