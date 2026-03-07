import { API_URL } from "./config.js";

fetch("header.html")
  .then(res => res.text())
  .then(data => document.getElementById("header").innerHTML = data);
fetch("footer.html")
  .then(res => res.text())
  .then(data => document.getElementById("footer").innerHTML = data);



async function checkBackend() {
    try {
          const response = await fetch(`${API_URL}/health/`);
        if (response.ok) {
            console.log("Servidor online...");

            return;
        }
    } catch (error) {
        console.log("Servidor dormindo...");
        window.location.href = "loading.html";

    }

    setTimeout(checkBackend, 5000);
}

function carregarProjetos() {
  fetch(`${API_URL}/api/dev/projetos/`)
    .then(response => response.json())
    .then(data => {

      const container = document.getElementById("projetos-container");

      container.innerHTML = "";

      data.forEach(projeto => {
        container.innerHTML += `
          <div class="card-projetos">
            <h3>${projeto.titulo}</h3>
            <img src="${projeto.imagem}" alt="${projeto.titulo}">
            <p>${projeto.descricao}</p>
            <div class="botoes-card">
              <a href="${projeto.link}" target="_blank" class="btn-projeto">Ver Projeto</a>
              <a href="${projeto.codigo}" target="_blank"class="btn-projeto">Código</a>
            </div>
          </div>
        `;
      });

    })
    .catch(error => console.error("Erro:", error));
}

function carregarCertificacoes(ordem) {
  fetch(`${API_URL}/api/dev/certificacoes/?ordering=${ordem}`)
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById("certificacoes-container");
      container.innerHTML = "";

      data.forEach(certificacao => {
        container.innerHTML += `
          <li class="card-certificacao">
            <div class="title-certificacao">
              <h3>${certificacao.titulo}</h3>
              <h4>${certificacao.instituicao}</h4>
            </div>
            <h5>Emitido em ${certificacao.emitido_em}</h5>
          </li>
        `;
      });
    });
}

checkBackend();
carregarProjetos();
carregarCertificacoes('-emitido_em')