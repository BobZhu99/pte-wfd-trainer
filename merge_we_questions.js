// 同题关系经题目文本核对后登记在配置中；不按标题相似度自动合并。
const config = require('./we_high_frequency_ids.json');
const englishQuestions = require('./we_english_questions.json');

function mergeWeQuestions(records) {
  const orderedIds = [...config.melon.map(id => 'M' + id), ...config.firefly.map(id => 'F' + id)];
  const allowed = new Set(orderedIds);
  const byId = new Map();
  for (const record of records) {
    for (const variant of record.variants || [record]) {
      if (!allowed.has(variant.qid)) continue;
      if (byId.has(variant.qid)) throw new Error('WE 题号重复：' + variant.qid);
      byId.set(variant.qid, variant);
    }
  }
  const missing = orderedIds.filter(id => !byId.has(id));
  if (missing.length) throw new Error('高频题缺失 ' + missing.join(', ') + '；保留原有 WE 题库');

  const pairs = new Map();
  for (const [melon, firefly] of config.merge_pairs) {
    if (!allowed.has(melon) || !allowed.has(firefly) || pairs.has(melon) || pairs.has(firefly)) {
      throw new Error('WE 合并映射无效：' + melon + ', ' + firefly);
    }
    pairs.set(melon, firefly);
    pairs.set(firefly, melon);
  }

  const consumed = new Set();
  const merged = [];
  for (const id of orderedIds) {
    if (consumed.has(id)) continue;
    const qids = pairs.has(id) ? [id, pairs.get(id)] : [id];
    qids.forEach(qid => consumed.add(qid));
    const variants = qids.map(qid => ({ ...byId.get(qid), ...(englishQuestions[qid] || {}) }));
    const primary = variants.find(item => item.qid.startsWith('F')) || variants[0];
    variants.filter(item => item.qid.startsWith('M')).forEach(item => {
      item.title_en = primary.title_en;
      item.shared_prompt_en = primary.prompt;
      item.shared_prompt_source_qid = primary.qid;
    });
    merged.push({
      index: merged.length + 1,
      qid: primary.qid,
      qids,
      title: primary.title,
      title_en: primary.title_en,
      prompt: primary.prompt,
      prompt_zh: primary.prompt_zh,
      prompt_source: primary.prompt_source,
      prompt_variants: primary.prompt_variants || [],
      sample_essay: primary.sample_essay || '',
      source: [...new Set(variants.map(item => item.source))].join(' + '),
      is_overlap: variants.length > 1,
      merge_note: qids.map(qid => (config.notes || {})[qid]).filter(Boolean).join(' '),
      variants
    });
  }
  return merged;
}

module.exports = { mergeWeQuestions };
