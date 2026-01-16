// AWS Lambda (Node.js 18+/20+). Handler para API Gateway (HTTP API o REST API).
// Uso (ejemplos):
// GET  /calc?op=add&a=2&b=3
// POST /calc  { "op": "div", "a": 10, "b": 2 }

export const handler = async (event) => {
  try {
    // 1) Leer entrada desde querystring o body JSON
    const qs = event?.queryStringParameters ?? {};
    let body = {};
    if (event?.body) {
      body = typeof event.body === "string" ? JSON.parse(event.body) : event.body;
    }

    const op = (body.op ?? qs.op ?? "").toString().trim().toLowerCase();
    const aRaw = body.a ?? qs.a;
    const bRaw = body.b ?? qs.b;

    const a = Number(aRaw);
    const b = Number(bRaw);

    // 2) Validaciones
    if (!op) return json(400, { error: "Falta 'op' (add|sub|mul|div|mod|pow)." });
    if (!Number.isFinite(a) || !Number.isFinite(b)) {
      return json(400, { error: "'a' y 'b' deben ser números válidos.", received: { a: aRaw, b: bRaw } });
    }

    // 3) Operaciones
    const ops = {
      add: (x, y) => x + y,
      sub: (x, y) => x - y,
      mul: (x, y) => x * y,
      div: (x, y) => {
        if (y === 0) throw httpError(400, "No se puede dividir entre 0.");
        return x / y;
      },
      mod: (x, y) => {
        if (y === 0) throw httpError(400, "No se puede hacer módulo entre 0.");
        return x % y;
      },
      pow: (x, y) => x ** y,
    };

    // Alias opcionales
    const aliases = { suma: "add", sumar: "add", resta: "sub", mult: "mul", multiplicar: "mul", dividir: "div" };
    const normalizedOp = ops[op] ? op : aliases[op];

    if (!normalizedOp || !ops[normalizedOp]) {
      return json(400, { error: "Operación no válida.", allowed: Object.keys(ops) });
    }

    const result = ops[normalizedOp](a, b);

    return json(200, { op: normalizedOp, a, b, result });
  } catch (err) {
    // Errores controlados vs inesperados
    if (err?.statusCode) return json(err.statusCode, { error: err.message });
    return json(500, { error: "Error interno.", details: String(err?.message ?? err) });
  }
};

function json(statusCode, payload) {
  return {
    statusCode,
    headers: { "content-type": "application/json; charset=utf-8" },
    body: JSON.stringify(payload),
  };
}

function httpError(statusCode, message) {
  const e = new Error(message);
  e.statusCode = statusCode;
  return e;
}
