function isCpf(cpf) {
    const regexForReplace = /\.|-/g;
    cpf = cpf.replace(regexForReplace, '');

    const regexForRepeatedChars = /(^\w{1})\1{10}/;
    if (cpf.match(regexForRepeatedChars)) return false;

    const digitCheck = (cpf, multiplier) => {
        let [i, m, sum] = [0, multiplier, 0];
        for (m; m > 1; m--) {
            sum += cpf[i] * m;
            i++;
        }
        let result = (sum * 10) % 11;
        result = result === 10 ? 0 : result;
        return result;
    };

    const firstDigitCheck = digitCheck(cpf, 10);
    const secondDigitCheck = digitCheck(cpf, 11);

    if (firstDigitCheck == cpf[9] && secondDigitCheck == cpf[10]) {
        return true;
    }
    return false;
}
