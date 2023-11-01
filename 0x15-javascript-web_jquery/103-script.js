$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

const translate = function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $.getJSON(url + $('INPUT#language_code').val(), function (data) {
    $('DIV#hello').html(data.hello);
  });
};
