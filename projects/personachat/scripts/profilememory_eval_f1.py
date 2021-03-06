from download_models import build
from parlai.core.params import ParlaiParser
from examples.eval_model import eval_model
from projects.personachat.persona_seq2seq import PersonachatSeqseqAgentSplit

'''Evaluate pre-trained model trained for f1 metric
Profile memory model trained on personachat using persona 'self'
Run from ParlAI directory
'''

if __name__ == '__main__':
    parser = ParlaiParser(add_model_args=True)
    parser.add_argument('-n', '--num-examples', default=100000000)
    parser.add_argument('-d', '--display-examples', type='bool', default=False)
    parser.add_argument('-ltim', '--log-every-n-secs', type=float, default=2)
    parser.set_defaults(
        task='personachat:self',
        model='projects.personachat.persona_seq2seq:PersonachatSeqseqAgentSplit',
        model_file='data/models/personachat/profile_memory/profilememory_mem2_reweight_sharelt_encdropout0.2_selfpersona_useall_attn_general_lstm_1024_1_1e-3_0.1',
        datatype='test'
    )
    PersonachatSeqseqAgentSplit.add_cmdline_args(parser)

    opt = parser.parse_args()
    opt['model_type'] = 'profile_memory'
    # build all profile memory models
    fnames = ['profilememory_mem2_reweight_sharelt_encdropout0.2_selfpersona_useall_attn_general_lstm_1024_1_1e-3_0.1',
              'profilememory_learnreweight_sharelt_encdropout0.4_s2s_usepersona_self_useall_attn_general_lstm_1024_1_1e-3_0.1',
              'fulldict.dict']
    build(opt, fnames)

    # add additional model args
    opt['dict_file'] = 'data/models/personachat/profile_memory/fulldict.dict'
    opt['rank_candidates'] = True

    eval_model(opt, parser)
