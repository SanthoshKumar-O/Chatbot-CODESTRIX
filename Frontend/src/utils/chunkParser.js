export const parseChunks = (sources) => {
  // given sources metadata, return readable lines
  if (!sources) return []
  return sources.map((s) => `${s.name} (chunk ${s.chunk || s.index || '?'})`)
}
