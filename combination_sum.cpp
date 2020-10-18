#include <vector>

class Solution {
public:
    
    void sol(vector<vector<int>>& res, vector<int>& v, vector<int>& candidates, int target, int curr){
        // found a combination
        if (target == 0) {
            res.push_back(v);
            return;
        }
        
        // missed a combination, backtrack
        if (target < 0) {
            return;
        }
        
        // keep progressing
        else {
            for (int i = curr; i < candidates.size(); i++) {
                if (candidates[i] <= target) {
                    v.push_back(candidates[i]);
                    sol(res, v, candidates, target - candidates[i], i);
                    v.pop_back(); // backtrack
                }
                else break;
            }
        }
        
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> v;
        sort(candidates.begin(), candidates.end());
        sol(res, v, candidates, target, 0);
        return res;
    }
};