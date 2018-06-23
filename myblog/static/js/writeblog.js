$(function () {
    var E = window.wangEditor;
    var editor = new E('#article-content');
    editor.create();

    $('[name=reset]').on('click', function () {
        $('input[name=headline]').val('');
        editor.txt.clear();
    })

    $('[name=submit]').on('click', function () {
        id = $('input[name=articleid]').val();
        title = $('input[name=headline]').val();
        desc = $('input[name=desc]').val();
        content = editor.txt.html();
        words = editor.txt.text().length;
        article = {'id': id, 'title': title, 'desc': desc, 'content': content, 'words': words}

        $.ajax({
            url: 'write',
            method: 'POST',
            data: article,
            success: function (data) {
                if (data['status'] == 200) {
                    location.href = '/blogs'
                }
            }
        })
    })
})