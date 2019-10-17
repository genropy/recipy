# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('alimento',name_long='alimento',name_plural='alimento',pkey='id',caption_field='nome')
        tbl.column('id',name_long='id',legacy_name='id')
        tbl.column('id_v_40',name_long='id_v_40',legacy_name='id_v_40')
        tbl.column('id_swissfir',name_long='id_swissfir',legacy_name='id_swissfir')
        tbl.column('nome',name_long='nome',legacy_name='nome')
        tbl.column('sinonimi',name_long='sinonimi',legacy_name='sinonimi')
        tbl.column('categoria',name_long='categoria',legacy_name='categoria')
        tbl.column('densita',name_long='densita',legacy_name='densita')
        tbl.column('unita_di_riferimento',name_long='unita_di_riferimento',legacy_name='unita_di_riferimento')
        tbl.column('energia_kilojoules',name_long='energia_kilojoules',legacy_name='energia_kilojoules')
        tbl.column('energia_calorie',name_long='energia_calorie',legacy_name='energia_calorie')
        tbl.column('lipidi_totali_g',name_long='lipidi_totali_g',legacy_name='lipidi_totali_g')
        tbl.column('acidi_grassi_saturi_g',name_long='acidi_grassi_saturi_g',legacy_name='acidi_grassi_saturi_g')
        tbl.column('acidi_grassi_monoinsaturi_g',name_long='acidi_grassi_monoinsaturi_g',legacy_name='acidi_grassi_monoinsaturi_g')
        tbl.column('acidi_grassi_polinsaturi_g',name_long='acidi_grassi_polinsaturi_g',legacy_name='acidi_grassi_polinsaturi_g')
        tbl.column('colesterolo_mg',name_long='colesterolo_mg',legacy_name='colesterolo_mg')
        tbl.column('glucidi_disponibili_g',name_long='glucidi_disponibili_g',legacy_name='glucidi_disponibili_g')
        tbl.column('zuccheri_g',name_long='zuccheri_g',legacy_name='zuccheri_g')
        tbl.column('amido_g',name_long='amido_g',legacy_name='amido_g')
        tbl.column('fibra_alimentare_g',name_long='fibra_alimentare_g',legacy_name='fibra_alimentare_g')
        tbl.column('proteine_g',name_long='proteine_g',legacy_name='proteine_g')
        tbl.column('sale_nacl_g',name_long='sale_nacl_g',legacy_name='sale_nacl_g')
        tbl.column('alcool_g',name_long='alcool_g',legacy_name='alcool_g')
        tbl.column('acqua_g',name_long='acqua_g',legacy_name='acqua_g')
        tbl.column('attivita_di_vitamina_a_re_g_re',name_long='attivita_di_vitamina_a_re_g_re',legacy_name='attivita_di_vitamina_a_re_g_re')
        tbl.column('attivita_di_vitamina_a_rae_g_re',name_long='attivita_di_vitamina_a_rae_g_re',legacy_name='attivita_di_vitamina_a_rae_g_re')
        tbl.column('equivalenti_di_all_trans_retinolo_g_re',name_long='equivalenti_di_all_trans_retinolo_g_re',legacy_name='equivalenti_di_all_trans_retinolo_g_re')
        tbl.column('attivita_di_beta_carotene_g_bce',name_long='attivita_di_beta_carotene_g_bce',legacy_name='attivita_di_beta_carotene_g_bce')
        tbl.column('beta_carotene_g',name_long='beta_carotene_g',legacy_name='beta_carotene_g')
        tbl.column('vitamina_b1_tiamina_mg',name_long='vitamina_b1_tiamina_mg',legacy_name='vitamina_b1_tiamina_mg')
        tbl.column('vitamina_b2_riboflavina_mg',name_long='vitamina_b2_riboflavina_mg',legacy_name='vitamina_b2_riboflavina_mg')
        tbl.column('vitamina_b6_piridossina_mg',name_long='vitamina_b6_piridossina_mg',legacy_name='vitamina_b6_piridossina_mg')
        tbl.column('vitamina_b12_cobalamina_g',name_long='vitamina_b12_cobalamina_g',legacy_name='vitamina_b12_cobalamina_g')
        tbl.column('niacina_mg',name_long='niacina_mg',legacy_name='niacina_mg')
        tbl.column('folati_g',name_long='folati_g',legacy_name='folati_g')
        tbl.column('acido_pantotenico_mg',name_long='acido_pantotenico_mg',legacy_name='acido_pantotenico_mg')
        tbl.column('vitamina_c_acido_ascorbico_mg',name_long='vitamina_c_acido_ascorbico_mg',legacy_name='vitamina_c_acido_ascorbico_mg')
        tbl.column('vitamina_d_calciferolo_g',name_long='vitamina_d_calciferolo_g',legacy_name='vitamina_d_calciferolo_g')
        tbl.column('attivita_di_vitamina_e_mg_ate',name_long='attivita_di_vitamina_e_mg_ate',legacy_name='attivita_di_vitamina_e_mg_ate')
        tbl.column('potassio_k_mg',name_long='potassio_k_mg',legacy_name='potassio_k_mg')
        tbl.column('sodio_na_mg',name_long='sodio_na_mg',legacy_name='sodio_na_mg')
        tbl.column('cloro_cl_mg',name_long='cloro_cl_mg',legacy_name='cloro_cl_mg')
        tbl.column('calcio_ca_mg',name_long='calcio_ca_mg',legacy_name='calcio_ca_mg')
        tbl.column('magnesio_mg_mg',name_long='magnesio_mg_mg',legacy_name='magnesio_mg_mg')
        tbl.column('fosforo_p_mg',name_long='fosforo_p_mg',legacy_name='fosforo_p_mg')
        tbl.column('ferro_fe_mg',name_long='ferro_fe_mg',legacy_name='ferro_fe_mg')
        tbl.column('iodio_i_g',name_long='iodio_i_g',legacy_name='iodio_i_g')
        tbl.column('zinco_zn_mg',name_long='zinco_zn_mg',legacy_name='zinco_zn_mg')
        tbl.column('selenio_se_g',name_long='selenio_se_g',legacy_name='selenio_se_g')
        tbl.column('voce_modificata',name_long='voce_modificata',legacy_name='voce_modificata')
