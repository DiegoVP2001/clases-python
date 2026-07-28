const fs = require("fs");
const path = require("path");

const outputDir = __dirname;
const pdfPath = path.join(outputDir, "kahoot_preguntas_python_hasta_if.pdf");
const csvPath = path.join(outputDir, "kahoot_preguntas_python_hasta_if.csv");

const questions = [
  {
    topic: "print",
    q: "¿Qué instrucción muestra un mensaje en pantalla?",
    options: ["input()", "print()", "int()", "bool()"],
    answer: "B",
  },
  {
    topic: "print",
    q: "¿Qué imprime este código? print('Hola', 'curso')",
    options: ["Holacurso", "Hola curso", "Hola, curso", "'Hola' 'curso'"],
    answer: "B",
  },
  {
    topic: "print",
    q: "¿Qué hace el parámetro sep en print()?",
    options: [
      "Define el separador entre valores impresos",
      "Convierte texto a número",
      "Detiene el programa",
      "Borra una variable",
    ],
    answer: "A",
  },
  {
    topic: "print",
    q: "¿Qué logra end=' ' en un print()?",
    options: [
      "Que el siguiente print continúe en la misma línea",
      "Que el texto se convierta en entero",
      "Que aparezca una línea vacía antes",
      "Que Python ignore el print",
    ],
    answer: "A",
  },
  {
    topic: "variables",
    q: "¿Cuál es un buen nombre de variable en Python?",
    options: ["2saldo", "saldo cuenta", "saldo_cuenta", "if"],
    answer: "C",
  },
  {
    topic: "variables",
    q: "¿Qué valor queda en saldo? saldo = 1000; saldo = saldo + 500",
    options: ["500", "1000", "1500", "saldo + 500"],
    answer: "C",
  },
  {
    topic: "números",
    q: "¿Qué operador se usa para multiplicar en Python?",
    options: ["x", "*", "·", "**"],
    answer: "B",
  },
  {
    topic: "números",
    q: "¿Qué resultado da 10 % 3?",
    options: ["1", "3", "3.33", "10"],
    answer: "A",
  },
  {
    topic: "comentarios",
    q: "¿Qué hace Python con una línea que empieza con #?",
    options: [
      "La ejecuta dos veces",
      "La usa como entrada",
      "La ignora como comentario",
      "La convierte en string",
    ],
    answer: "C",
  },
  {
    topic: "input",
    q: "¿Qué tipo de dato devuelve input() antes de convertirlo?",
    options: ["int", "float", "bool", "str"],
    answer: "D",
  },
  {
    topic: "input",
    q: "Si quieres calcular con una edad ingresada por teclado, ¿qué opción corresponde?",
    options: [
      "edad = input() + int",
      "edad = int(input())",
      "edad = print(input())",
      "edad = bool(input())",
    ],
    answer: "B",
  },
  {
    topic: "input",
    q: "¿Qué conversión conviene para guardar 12.5 horas jugadas?",
    options: ["int()", "float()", "bool()", "print()"],
    answer: "B",
  },
  {
    topic: "errores",
    q: "¿Qué problema aparece al intentar hacer input() + 10 sin convertir?",
    options: [
      "Se suma correctamente",
      "Python interpreta 10 como texto automáticamente",
      "Puede producir TypeError",
      "Siempre devuelve True",
    ],
    answer: "C",
  },
  {
    topic: "booleanos",
    q: "¿Cómo se escribe verdadero en Python?",
    options: ["true", "TRUE", "True", "verdadero"],
    answer: "C",
  },
  {
    topic: "comparaciones",
    q: "¿Qué operador compara si dos valores son iguales?",
    options: ["=", "==", "!=", ">="],
    answer: "B",
  },
  {
    topic: "comparaciones",
    q: "¿Qué resultado da 45000 >= 60000?",
    options: ["True", "False", "45000", "Error siempre"],
    answer: "B",
  },
  {
    topic: "comparaciones",
    q: "La regla dice: 'edad de 18 o más'. ¿Qué condición representa mejor la regla?",
    options: ["edad > 18", "edad >= 18", "edad == 18", "edad < 18"],
    answer: "B",
  },
  {
    topic: "bool",
    q: "¿Qué resultado da bool(0)?",
    options: ["True", "False", "0", "None"],
    answer: "B",
  },
  {
    topic: "bool",
    q: "¿Qué resultado da bool(-3)?",
    options: ["True", "False", "-3", "Error"],
    answer: "A",
  },
  {
    topic: "and",
    q: "¿Cuándo devuelve True el operador and?",
    options: [
      "Cuando al menos una condición es True",
      "Solo cuando ambas condiciones son True",
      "Solo cuando ambas condiciones son False",
      "Cuando se usa con números",
    ],
    answer: "B",
  },
  {
    topic: "or",
    q: "¿Qué resultado da True or False?",
    options: ["True", "False", "Error", "None"],
    answer: "A",
  },
  {
    topic: "not",
    q: "¿Qué resultado da not True?",
    options: ["True", "False", "0", "1"],
    answer: "B",
  },
  {
    topic: "operadores lógicos",
    q: "Para publicar se necesita cuenta activa y no estar suspendido. ¿Cuál condición es correcta?",
    options: [
      "cuenta_activa or suspendido",
      "cuenta_activa and suspendido",
      "cuenta_activa and not suspendido",
      "not cuenta_activa and suspendido",
    ],
    answer: "C",
  },
  {
    topic: "operadores lógicos",
    q: "Recibes notificación si estás en el servidor o si te mencionaron. ¿Qué operador corresponde?",
    options: ["and", "or", "not", "=="],
    answer: "B",
  },
  {
    topic: "casos límite",
    q: "La regla dice: 'descuento para compras de $15000 o más'. ¿Con qué valor hay que probar el caso límite?",
    options: ["14999", "15000", "15001", "0"],
    answer: "B",
  },
  {
    topic: "casos límite",
    q: "Si una nota 4.0 aprueba, ¿qué condición es más precisa?",
    options: ["nota > 4.0", "nota >= 4.0", "nota == 7.0", "nota < 4.0"],
    answer: "B",
  },
  {
    topic: "if",
    q: "¿Qué hace un if en Python?",
    options: [
      "Ejecuta un bloque solo si la condición es True",
      "Ejecuta siempre los dos bloques",
      "Convierte texto a número",
      "Repite el código muchas veces",
    ],
    answer: "A",
  },
  {
    topic: "else",
    q: "¿Cuándo se ejecuta el bloque else?",
    options: [
      "Cuando la condición del if es True",
      "Cuando la condición del if es False",
      "Antes del if",
      "Solo si hay input()",
    ],
    answer: "B",
  },
  {
    topic: "sintaxis",
    q: "¿Qué símbolo debe ir al final de una línea con if condicion?",
    options: [".", ";", ":", ","],
    answer: "C",
  },
  {
    topic: "indentación",
    q: "¿Por qué es importante indentar el bloque debajo de if o else?",
    options: [
      "Porque Python usa la indentación como parte de la sintaxis",
      "Porque mejora solo el color del código",
      "Porque convierte los valores en booleanos",
      "Porque evita usar print()",
    ],
    answer: "A",
  },
];

function csvEscape(value) {
  return `"${String(value).replace(/"/g, '""')}"`;
}

function writeCsv() {
  const header = ["N", "Pregunta", "Alternativa A", "Alternativa B", "Alternativa C", "Alternativa D", "Correcta", "Tema"];
  const rows = questions.map((item, index) => [
    index + 1,
    item.q,
    item.options[0],
    item.options[1],
    item.options[2],
    item.options[3],
    item.answer,
    item.topic,
  ]);
  const csv = [header, ...rows].map((row) => row.map(csvEscape).join(";")).join("\r\n");
  fs.writeFileSync(csvPath, "\uFEFF" + csv, "utf8");
}

function sanitizePdfText(text) {
  return String(text)
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/[–—]/g, "-")
    .replace(/[→]/g, "->")
    .replace(/[≥]/g, ">=")
    .replace(/[≤]/g, "<=")
    .replace(/[•]/g, "-")
    .replace(/[^\x09\x0A\x0D\x20-\x7E\xA0-\xFF]/g, "");
}

function escapePdfString(text) {
  return sanitizePdfText(text).replace(/\\/g, "\\\\").replace(/\(/g, "\\(").replace(/\)/g, "\\)");
}

function wrapText(text, maxChars) {
  const paragraphs = sanitizePdfText(text).split(/\r?\n/);
  const lines = [];
  for (const paragraph of paragraphs) {
    const words = paragraph.split(/\s+/).filter(Boolean);
    let line = "";
    for (const word of words) {
      if (!line) {
        line = word;
      } else if ((line + " " + word).length <= maxChars) {
        line += " " + word;
      } else {
        lines.push(line);
        line = word;
      }
    }
    if (line) lines.push(line);
    if (!words.length) lines.push("");
  }
  return lines;
}

function buildPages() {
  const pageWidth = 595;
  const pageHeight = 842;
  const margin = 46;
  const bottom = 48;
  const pages = [];
  let page = [];
  let y = pageHeight - margin;

  function newPage() {
    page = [];
    pages.push(page);
    y = pageHeight - margin;
  }

  function addLine(text, options = {}) {
    const size = options.size || 10;
    const leading = options.leading || Math.round(size * 1.45);
    const font = options.font || "F1";
    const x = options.x || margin;
    if (y < bottom + leading) newPage();
    page.push({ text: sanitizePdfText(text), x, y, font, size });
    y -= leading;
  }

  function addWrapped(text, options = {}) {
    const size = options.size || 10;
    const maxChars = options.maxChars || Math.floor((pageWidth - margin * 2) / (size * 0.47));
    for (const line of wrapText(text, maxChars)) {
      addLine(line, options);
    }
  }

  newPage();
  addLine("Banco de preguntas tipo Kahoot", { font: "F2", size: 18, leading: 24 });
  addLine("Python - corte curricular hasta if / else", { font: "F2", size: 12, leading: 18 });
  addWrapped(
    "30 preguntas de respuesta rápida, 4 alternativas cada una. Contenidos: fundamentos, variables, comentarios, print(), input(), conversiones, booleanos, comparadores, operadores lógicos, casos límite, if / else e indentación.",
    { size: 10, leading: 14 }
  );
  addLine("Tiempo sugerido por pregunta: 20 a 30 segundos.", { size: 10, leading: 18 });
  addLine("Preguntas", { font: "F2", size: 14, leading: 22 });

  questions.forEach((item, index) => {
    if (y < 150) newPage();
    addWrapped(`${index + 1}. ${item.q}`, { font: "F2", size: 10.5, leading: 14, maxChars: 86 });
    ["A", "B", "C", "D"].forEach((letter, optIndex) => {
      addWrapped(`${letter}) ${item.options[optIndex]}`, {
        size: 9.5,
        leading: 13,
        x: margin + 12,
        maxChars: 88,
      });
    });
    addLine("", { size: 5, leading: 6 });
  });

  newPage();
  addLine("Pauta de respuestas", { font: "F2", size: 16, leading: 24 });
  addWrapped("Usa esta tabla para configurar la alternativa correcta en Kahoot.", { size: 10, leading: 16 });
  questions.forEach((item, index) => {
    const correct = item.options["ABCD".indexOf(item.answer)];
    addWrapped(`${index + 1}. ${item.answer}) ${correct}`, { size: 10, leading: 14, maxChars: 96 });
  });

  return { pages, pageWidth, pageHeight };
}

function latin1Buffer(text) {
  return Buffer.from(sanitizePdfText(text), "latin1");
}

function writePdf() {
  const { pages, pageWidth, pageHeight } = buildPages();
  const objects = [];

  function addObject(content) {
    objects.push(content);
    return objects.length;
  }

  const catalogId = addObject("");
  const pagesId = addObject("");
  const fontRegularId = addObject("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>");
  const fontBoldId = addObject("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>");

  const pageIds = [];
  const contentIds = [];

  pages.forEach((pageItems, pageIndex) => {
    const ops = [];
    if (pageIndex > 0) {
      // Repeated running header.
      pageItems.unshift({
        text: "Banco Kahoot Python hasta if / else",
        x: 46,
        y: pageHeight - 28,
        font: "F2",
        size: 8,
      });
    }
    pageItems.push({
      text: `Página ${pageIndex + 1} de ${pages.length}`,
      x: pageWidth - 112,
      y: 28,
      font: "F1",
      size: 8,
    });
    for (const item of pageItems) {
      ops.push(`BT /${item.font} ${item.size} Tf ${item.x} ${item.y} Td (${escapePdfString(item.text)}) Tj ET\n`);
    }
    const streamBytes = latin1Buffer(ops.join(""));
    const contentId = addObject(Buffer.concat([
      Buffer.from(`<< /Length ${streamBytes.length} >>\nstream\n`, "ascii"),
      streamBytes,
      Buffer.from("\nendstream", "ascii"),
    ]));
    contentIds.push(contentId);
    const pageId = addObject("");
    pageIds.push(pageId);
  });

  objects[catalogId - 1] = `<< /Type /Catalog /Pages ${pagesId} 0 R >>`;
  objects[pagesId - 1] = `<< /Type /Pages /Kids [${pageIds.map((id) => `${id} 0 R`).join(" ")}] /Count ${pageIds.length} >>`;

  pageIds.forEach((pageId, index) => {
    objects[pageId - 1] =
      `<< /Type /Page /Parent ${pagesId} 0 R /MediaBox [0 0 ${pageWidth} ${pageHeight}] ` +
      `/Resources << /Font << /F1 ${fontRegularId} 0 R /F2 ${fontBoldId} 0 R >> >> ` +
      `/Contents ${contentIds[index]} 0 R >>`;
  });

  const chunks = [Buffer.from("%PDF-1.4\n%\xE2\xE3\xCF\xD3\n", "binary")];
  const offsets = [0];
  objects.forEach((objectContent, index) => {
    offsets[index + 1] = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
    chunks.push(Buffer.from(`${index + 1} 0 obj\n`, "ascii"));
    chunks.push(Buffer.isBuffer(objectContent) ? objectContent : latin1Buffer(objectContent));
    chunks.push(Buffer.from("\nendobj\n", "ascii"));
  });

  const xrefOffset = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
  const xref = [
    "xref",
    `0 ${objects.length + 1}`,
    "0000000000 65535 f ",
    ...offsets.slice(1).map((offset) => `${String(offset).padStart(10, "0")} 00000 n `),
    "trailer",
    `<< /Size ${objects.length + 1} /Root ${catalogId} 0 R >>`,
    "startxref",
    String(xrefOffset),
    "%%EOF",
    "",
  ].join("\n");
  chunks.push(Buffer.from(xref, "ascii"));
  fs.writeFileSync(pdfPath, Buffer.concat(chunks));
}

writeCsv();
writePdf();

console.log(`PDF generado: ${pdfPath}`);
console.log(`CSV generado: ${csvPath}`);
console.log(`Total preguntas: ${questions.length}`);
