// Dicas visuais simples para raça e classe
const RACE_HINTS = {
  humano: "+1 CAR, Adaptável, Versátil",
  elfo: "+1 DES, Visão no Escuro, Sentidos Aguçados",
  anao: "+1 CON, Resiliência, Conhecimento de Pedra",
};
const CLASS_HINTS = {
  guerreiro: "Atributo-chave: FOR • Ataque Extra, Estilo de Combate",
  mago: "Atributo-chave: INT • Magia Arcana, Preparar Feitiços",
  ladino: "Atributo-chave: DES • Ataque Furtivo, Evasão",
};

function hint(selectId, hintId, dict){
  const sel = document.getElementById(selectId);
  const hint = document.getElementById(hintId);
  if(!sel || !hint) return;
  const update = () => { hint.textContent = dict[sel.value] || ""; };
  sel.addEventListener('change', update);
  update();
}

document.addEventListener('DOMContentLoaded', () => {
  hint('racaSelect', 'raceHint', RACE_HINTS);
  hint('classeSelect', 'classHint', CLASS_HINTS);
});
