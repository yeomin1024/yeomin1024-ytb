// 숫자 표기 (만 원 단위 → "8,000만 원")
export const won = (man: number, sign = false) => {
  const v = Math.round(man);
  if (v === 0) return "0원";
  const s = Math.abs(v).toLocaleString("ko-KR");
  return `${v < 0 ? "-" : sign && v > 0 ? "+" : ""}${s}만 원`;
};
export const num = (v: number, digits = 0) => v.toLocaleString("ko-KR", {minimumFractionDigits: digits, maximumFractionDigits: digits});
/** 만 단위 정수 → "8억 2,700만" */
export const eokMan = (man: number) => {
  const v = Math.round(Math.abs(man));
  const eok = Math.floor(v / 10000);
  const rest = v % 10000;
  const s = [eok ? `${eok}억` : "", rest ? `${rest.toLocaleString("ko-KR")}만` : ""].filter(Boolean).join(" ") || "0";
  return `${man < 0 ? "-" : ""}${s}`;
};
