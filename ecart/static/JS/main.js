var script= document.createElement('script')

script.type= 'text/javascript';
script.src= "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

console.log('This is working..')

script.onload = function() {

    var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    console.log('This is working.. Functions')

    tinymce.init({

      selector: '#id_content',
      plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker imagetools textpattern noneditable help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable export',
     
   
    });
    
    
    

}

