console.log("funcoes.js carregado com sucesso!");

function MinhaPrimeiraFuncao() {
    $('#area-01').css({
        color: '#ff0000',
        textTransform: 'uppercase',
        width: '70%'
    });
}

function MinhaSegundaFuncao() {
    $('#area-02').empty();

    var alunos = ['Aluno 01', 'Aluno 02'];

    $.each(alunos, function(index, value) {
        $('#area-02').append(value + '<br>');
    });
}

function MinhaTerceiraFuncao() {
    $('#area-01').html('A terceira função foi executada com sucesso!');
}