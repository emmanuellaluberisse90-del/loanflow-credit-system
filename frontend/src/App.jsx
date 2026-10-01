import { useState } from "react"
import "./App.css"

function App() {
  // PRÉ-ANÁLISE
  const [idSolicitacao, setIdSolicitacao] = useState("")
  const [analise, setAnalise] = useState(null)

  // SIMULAÇÃO
  const [valor, setValor] = useState("")
  const [prazo, setPrazo] = useState("")
  const [taxa, setTaxa] = useState("")
  const [simulacao, setSimulacao] = useState(null)

  // AGENDAMENTO
  const [agencias, setAgencias] = useState([])
  const [idAgencia, setIdAgencia] = useState("")
  const [horarios, setHorarios] = useState([])
  const [idHorario, setIdHorario] = useState("")
  const [agendamento, setAgendamento] = useState(null)

  const [erro, setErro] = useState("")

  async function consultarAnalise() {
    setErro("")
    setAnalise(null)

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/analises/?id_solicitacao=${idSolicitacao}`,
        {
          method: "POST"
        }
      )

      if (!response.ok) {
        const data = await response.json()
        throw new Error(
          data.detail || "Não foi possível realizar a pré-análise."
        )
      }

      const data = await response.json()
      setAnalise(data)
    } catch (error) {
      setErro(error.message)
    }
  }

  async function realizarSimulacao() {
    setErro("")
    setSimulacao(null)

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/simulacoes/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            id_solicitacao: Number(idSolicitacao),
            valor_simulado: Number(valor),
            prazo_meses: Number(prazo),
            taxa_mensal: Number(taxa)
          })
        }
      )

      if (!response.ok) {
        const data = await response.json()
        throw new Error(
          data.detail || "Não foi possível realizar a simulação."
        )
      }

      const data = await response.json()
      setSimulacao(data)
    } catch (error) {
      setErro(error.message)
    }
  }

  async function carregarAgencias() {
    setErro("")
    setAgendamento(null)

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/agencias/"
      )

      if (!response.ok) {
        throw new Error(
          "Não foi possível carregar as agências."
        )
      }

      const data = await response.json()
      setAgencias(data)
    } catch (error) {
      setErro(error.message)
    }
  }

  async function carregarHorarios(id) {
    setIdAgencia(id)
    setIdHorario("")
    setHorarios([])
    setAgendamento(null)
    setErro("")

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/horarios/?id_agencia=${id}`
      )

      if (!response.ok) {
        throw new Error(
          "Não foi possível carregar os horários."
        )
      }

      const data = await response.json()
      setHorarios(data)
    } catch (error) {
      setErro(error.message)
    }
  }

  async function realizarAgendamento() {
    setErro("")
    setAgendamento(null)

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/agendamentos/?id_cliente=1&id_solicitacao=${idSolicitacao}&id_agencia=${idAgencia}&id_horario=${idHorario}`,
        {
          method: "POST"
        }
      )

      if (!response.ok) {
        const data = await response.json()

        throw new Error(
          data.detail ||
          "Não foi possível realizar o agendamento."
        )
      }

      const data = await response.json()
      setAgendamento(data)
    } catch (error) {
      setErro(error.message)
    }
  }

  return (
    <div className="container">

      {/* CABEÇALHO */}

      <div className="header">
        <h1>LoanFlow</h1>

        <p>
          Sistema de Pré-análise, Simulação e Agendamento de Crédito
        </p>
      </div>


      {/* PRÉ-ANÁLISE */}

      <div className="card">
        <h2>Pré-análise</h2>

        <input
          type="number"
          placeholder="ID da solicitação"
          value={idSolicitacao}
          onChange={(e) =>
            setIdSolicitacao(e.target.value)
          }
        />

        <br />

        <button onClick={consultarAnalise}>
          Realizar pré-análise
        </button>

        {analise && (
          <div className="resultado">
            <h3>Resultado da pré-análise</h3>

            <p>
              <strong>Status:</strong>{" "}
              {analise.resultado}
            </p>

            <p>
              <strong>Comprometimento da renda:</strong>{" "}
              {(analise.comprometimento_renda * 100).toFixed(2)}%
            </p>

            <p>
              <strong>Valor máximo simulado:</strong>{" "}
              R$ {analise.valor_maximo_simulado.toFixed(2)}
            </p>

            <p>
              <strong>Motivo:</strong>{" "}
              {analise.motivo_resultado}
            </p>
          </div>
        )}
      </div>


      {/* SIMULAÇÃO */}

      <div className="card">
        <h2>Simulação</h2>

        <input
          type="number"
          placeholder="Valor do empréstimo"
          value={valor}
          onChange={(e) =>
            setValor(e.target.value)
          }
        />

        <br />

        <input
          type="number"
          placeholder="Prazo em meses"
          value={prazo}
          onChange={(e) =>
            setPrazo(e.target.value)
          }
        />

        <br />

        <input
          type="number"
          step="0.01"
          placeholder="Taxa mensal (%)"
          value={taxa}
          onChange={(e) =>
            setTaxa(e.target.value)
          }
        />

        <br />

        <button onClick={realizarSimulacao}>
          Simular empréstimo
        </button>

        {simulacao && (
          <div className="resultado">
            <h3>Resultado da simulação</h3>

            <p>
              <strong>Valor:</strong>{" "}
              R$ {simulacao.valor_simulado.toFixed(2)}
            </p>

            <p>
              <strong>Prazo:</strong>{" "}
              {simulacao.prazo_meses} meses
            </p>

            <p>
              <strong>Taxa mensal:</strong>{" "}
              {simulacao.taxa_mensal}%
            </p>

            <p>
              <strong>Valor da parcela:</strong>{" "}
              R$ {simulacao.valor_parcela.toFixed(2)}
            </p>

            <p>
              <strong>Valor total:</strong>{" "}
              R$ {simulacao.valor_total.toFixed(2)}
            </p>

            <p>
              <strong>Parcela compatível:</strong>{" "}
              {simulacao.parcela_compativel === "True"
                ? "Sim"
                : "Não"}
            </p>
          </div>
        )}
      </div>


      {/* AGENDAMENTO */}

      <div className="card">
        <h2>Agendamento</h2>

        <button onClick={carregarAgencias}>
          Carregar agências
        </button>

        <br />
        <br />

        {agencias.length > 0 && (
          <select
            value={idAgencia}
            onChange={(e) =>
              carregarHorarios(e.target.value)
            }
          >
            <option value="">
              Selecione uma agência
            </option>

            {agencias.map((agencia) => (
              <option
                key={agencia.id}
                value={agencia.id}
              >
                {agencia.nome_agencia} - {agencia.cidade}
              </option>
            ))}
          </select>
        )}

        <br />

        {horarios.length > 0 && (
          <select
            value={idHorario}
            onChange={(e) =>
              setIdHorario(e.target.value)
            }
          >
            <option value="">
              Selecione um horário
            </option>

            {horarios.map((horario) => (
              <option
                key={horario.id}
                value={horario.id}
              >
                {horario.data} - {horario.hora_inicio} às{" "}
                {horario.hora_fim}
              </option>
            ))}
          </select>
        )}

        <br />

        <button
          onClick={realizarAgendamento}
          disabled={
            !idAgencia ||
            !idHorario ||
            !idSolicitacao
          }
        >
          Agendar atendimento
        </button>


        {/* CONFIRMAÇÃO */}

        {agendamento && (
          <div className="sucesso">
            <h3>Agendamento realizado!</h3>

            <p>
              <strong>Agência:</strong>{" "}
              {agencias.find(
                (agencia) =>
                  String(agencia.id) === String(idAgencia)
              )?.nome_agencia}
            </p>

            <p>
              <strong>Data:</strong>{" "}
              {horarios.find(
                (horario) =>
                  String(horario.id) === String(idHorario)
              )?.data}
            </p>

            <p>
              <strong>Horário:</strong>{" "}
              {horarios.find(
                (horario) =>
                  String(horario.id) === String(idHorario)
              )?.hora_inicio}
              {" às "}
              {horarios.find(
                (horario) =>
                  String(horario.id) === String(idHorario)
              )?.hora_fim}
            </p>

            <p>
              <strong>Status:</strong>{" "}
              {agendamento.status}
            </p>

            <p>
              <strong>ID do agendamento:</strong>{" "}
              {agendamento.id}
            </p>
          </div>
        )}
      </div>


      {/* ERRO */}

      {erro && (
        <div className="erro">
          <strong>Erro:</strong>{" "}
          {erro}
        </div>
      )}

    </div>
  )
}

export default App