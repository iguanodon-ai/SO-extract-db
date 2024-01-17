import { Selectable } from "kysely";

type Definition = {
  description: string;
  subtitle: string; // To rename
  examples: string[];
  year: string | number;
  subDefinitions: Definition[];
};

type Entry = {
  key: number; // ort_snr
  word: string; // ortografie
  nature: string;
  internal_SO_info: number;
  definitions: Definition[];
};

export interface Database {
  superlemma: SuperlemmaTable;
  lemma: LemmaTable;
  betydelser: BetydelserTable;
  etymologier: EtymologierTable;
  syntex: SyntexTable;
}

export interface SuperlemmaTable {
  s_nr: number;
  ordklass: string;
  typ: string;
}

export interface LemmaTable {
  s_nr: number;
  wtype: string;
  origin: string;
  ortografi: string;
  lm_sabob: number;
}

export interface BetydelserTable {
  s_nr: number;
  x_nr: number;
  kc_nr: number;
  def: string;
  deft: string;
  typ: string;
  kcorder: number;
}

export interface EtymologierTable {
  x_nr: number;
  fbel: string;
  etymologi: string;
}

export interface SyntexTable {
  kc_nr: number;
  sx_text: string;
}

export type SuperLemma = Selectable<SuperlemmaTable>;
export type Lemma = Selectable<LemmaTable>;
export type Betydelser = Selectable<BetydelserTable>;
export type Etymologier = Selectable<EtymologierTable>;
export type Syntex = Selectable<SyntexTable>;
