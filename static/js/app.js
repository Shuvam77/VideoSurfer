// const uploadForm = document.getElementById('post-form')
// const input = document.getElementById('fileupload')
// const progressBox = document.getElementById('progress-box')
// const cancelBox = document.getElementById('cancel-box')
// const cancelBtn = document.getElementById('cancel-btn')
// const csrf = document.getElementsByName('csrfmiddlewretoken')

// input.addEventListener('change', ()=>{
//     progressBox.classList.remove('not-visible')
//     cancelBox.classList.remove('not-visible')

//     const fd = new FormData()
//     fd.append('csrfmiddlewretoken', csrf[0].value)
//     fd.append('title', title_data)
//     fd.append('video', video_data)

//     $.ajax({
//         type:'POST',
//         url: uploadForm.action,
//         enctype: 'multipart/form-data',
//         data: fd,
//         beforeSend: function(){

//         },
//         xhr: function(){
//             const xhr = new window.XMLHttpRequest();
//             xhr.upload.addEventListener('progress', e=>{
//                 if(e.lengthCoumputable){
//                     const percent = e.loaded / e.total * 100
//                     progressBox.innerHTML = `<div class="progress">
//                                                 <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}%" area-valuemin="0" aria-valuemax="100"></div>
//                                             </div>
//                                             <p>${percent.toFixed(1)}</p>`
//                 }
//             })
//             cancelBtn.addEventListener('click',()=>{
//                 xhr.abort(),
//                 setTimeout(()=>{
//                     uploadForm.reset()
//                     progressBox.innerHTML=""
//                     cancelBox.classList.add('not-visible')
//                 }, 2000)

//             })
//             return xhr

//         },
//         success: function(){
//             cancelBox.classList.add('not-visible')
//         },
//         cache: false,
//         contextType: false,
//         processData: false,
//     })
// })