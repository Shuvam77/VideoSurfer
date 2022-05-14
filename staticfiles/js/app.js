const uploadForm = document.getElementById('post-form')
const input = document.getElementById('fileupload')
const alertBox = document.getElementById('alert-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
const csrf = document.getElementsByName('csrfmiddlewretoken')

console.log(csrf)